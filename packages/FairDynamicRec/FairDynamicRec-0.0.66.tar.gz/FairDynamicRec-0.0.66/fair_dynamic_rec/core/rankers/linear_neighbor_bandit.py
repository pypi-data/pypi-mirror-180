import numpy as np
from .abstract_ranker import AbstractRanker

class NeighborUCB(AbstractRanker):
    def __init__(self, config, dataObj, parameters=None):
        super(NeighborUCB, self).__init__(config, dataObj)
        self.n_samples = np.zeros(dataObj.n_users)
        self.n_clicks = np.zeros(dataObj.n_users)
        self.prng = np.random.RandomState(seed=config.seed)
        self.sigma = float(parameters["sigma"]["value"]) if "sigma" in parameters else 1.0

        self.l = int(parameters["latent_dim"]["value"]) if "latent_dim" in parameters else 0
        self.lambda_1 = float(parameters["lambda"]["value"]) if "lambda" in parameters else 1.0
        self.alpha_v = float(parameters["alpha_v"]["value"]) if "alpha_v" in parameters else 1.0
        self.alpha_u = float(parameters["alpha_u"]["value"]) if "alpha_u" in parameters else 1.0

        self.X = dataObj.train_data

        # self.XTX = np.dot(self.X.T, self.X)

        self.U = np.zeros((self.dataObj.n_items, self.l))
        self.V = np.zeros((self.dataObj.n_items, self.l))

        # A = U_T * (X_T.X + lambda) * U      -> l * l
        self.A = np.eye(self.l)
        self.AInv = np.linalg.inv(self.A)

        # U_T * (X_T . X_{u,i} - dMat(\etha))   -> l * m
        self.b = np.zeros((self.l, dataObj.n_items))

        # X_T . X + \lambda                   -> m * m
        self.C = self.lambda_1 * np.eye(dataObj.n_items)
        self.CInv = np.linalg.inv(self.C)

        # (X_T . X + dMat(\etha)) * V          -> m * l
        self.d = np.zeros((dataObj.n_items, self.l))

        self.E = np.zeros((self.l, self.l))
        self.EInv = np.linalg.inv(self.E)


        self.ill_matrix_counter = 0
        # for ill inverse
        self.AInv_tmp = np.zeros((self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users))
        self.b_tmp = np.zeros((self.dataObj.n_users, (self.k + self.l) * self.dataObj.n_users))
        self.CInv_tmp = np.zeros((self.dataObj.n_items, self.l, self.l))
        self.d_tmp = np.zeros((self.dataObj.n_items, self.l))

    def get_ranking(self, batch_users, sampled_items=None, round=None):
        """
        :param x: features
        :param k: number of positions
        :return: ranking: the ranked item id.
        """
        # assert x.shape[0] >= k
        rankings = np.zeros((len(batch_users), self.config.list_size), dtype=int)
        # self.batch_features = np.zeros((len(batch_users), self.config.list_size, self.dim))
        tie_breaker = self.prng.rand(len(sampled_items))
        for i in range(len(batch_users)):
            user = batch_users[i]

            score = np.dot(self.X[user], np.dot(self.U, self.V.T))
            XU = np.multiply(self.X[user].T,self.U) # m * k
            cb1 = np.sqrt(np.sum(np.multiply(np.dot(XU, self.AInv), XU), axis=1))
            cb2 = np.sqrt(np.multiply(self.X[user].T, np.dot(self.CInv, self.X[user])))
            cb3 = np.sqrt(np.sum(np.multiply(np.dot(self.V, self.EInv), self.V), axis=1))

            ucb = score + self.alpha_u * cb1 + self.alpha_v * cb2 * cb3

            rankings[i] = np.lexsort((tie_breaker, -ucb))[:self.config.list_size]

        return rankings

    def update(self, batch_users, sampled_items, rankings, clicks, round=None, user_round=None):
        for i in range(len(batch_users)):
            user = batch_users[i]

            _clicks, _ranking = self.__collect_feedback(clicks[i], rankings[i])

            # discount_coef = [1 / (math.log(1 + j)) for j in range(1, len(rankings[0]) + 1)]
            # discount_coef_reward = [math.log(1 + j) for j in range(1, len(_clicks) + 1)]
            # discount_coef_penalization = [self.gamma * 1 / (math.log(1 + j)) for j in range(1, len(_clicks) + 1)]

            # if self.processing_type == 'recommended_discountfactor':
            #     self.exp_recommended[user][np.array(rankings[0])] += discount_coef
            # elif self.processing_type == 'examined_discountfactor':
            #     if len(clicks) == 0:
            #         self.exp_examined[user][np.array(rankings[0])] += discount_coef
            #     else:
            #         self.exp_examined[user][np.array(rankings[0][:len(clicks)])] += discount_coef[:len(clicks)]
            #
            # if self.processing_type == 'item_weight':
            #     _batch_features = self.update_item_weight(rankings[0], _batch_features, _clicks, discount_coef_penalization, discount_coef_reward, user, user_round)

            """
            This is for computing self.theta (Line 3-5 of Alogirthm 1 of NIPS 11)
            For fast matrix inverse, we use Woodbury matrix identity (https://en.wikipedia.org/wiki/Woodbury_matrix_identity)

            Return: self.theta is updated.
            """
            # for the inverse of M, feature matrix
            # XU * A^-1 * XW^T
            XU = np.multiply(self.X[user].T,self.U) # m * k
            xAx = np.dot(XU[_rankings], np.dot(self.AInv[user], XU[_rankings].T))
            # (1/sigma I + xAx)^-1
            try:
                tmp_inv = np.linalg.inv(1 / self.sigma * np.eye(len(XU[_rankings])) + xAx)
            except np.linalg.LinAlgError:
                # for the ill matrix. if the matrix is not invertible, we ignore this update
                self.ill_matrix_counter += 1
                return
            # A^-1*x^T
            AInv_xT = self.AInv[user].dot(_XVW_optimal.T)
            # AInv_xT*tmp_inv*AInv_xT^T
            self.AInv_tmp = np.dot(np.dot(AInv_xT, tmp_inv), AInv_xT.T)
            # MInv - the new part
            self.AInv[user] -= self.AInv_tmp
            self.A[user] += self.sigma * _XVW_optimal.T.dot(_XVW_optimal)

            # for b: feedback
            # if self.processing_type == 'feature_weight':
            #     self.update_feature_weight(_batch_features, _clicks, discount_coef_penalization, discount_coef_reward,
            #                                user, user_round)
            # else:
            self.b[user] += np.dot(_clicks, _XVW_optimal)
            # for parameter Theta
            self.Theta = self.devectorize(np.dot(self.AInv[user], self.b[user]), self.k+self.l)
            # self.theta[self.theta < 0] = 0
            self.Theta_x = self.Theta[:, :self.k]
            self.Theta_v = self.Theta[:, self.k:]


            ranking = rankings[i][:len(_clicks)]
            Theta_v_W = np.dot(self.Theta_v.T, self.W[user].T)
            xx = np.dot(Theta_v_W.reshape(self.Theta_v.shape[1],1), Theta_v_W.reshape(self.Theta_v.shape[1],1).T)
            for i in range(len(ranking)):
                item = ranking[i]
                self.C[item] += xx
                self.CInv[item] = np.linalg.inv(self.C[item])
                if self.contextual_var:
                    # print('a='+str(self.d.shape)+', b='+str(Theta_v_W.shape)+', c='+str(self.X[ranking].shape)+', d='+str(self.Theta_x.T.shape)+', e='+str(self.W[user])+', f='+str((_clicks[i] - np.dot(self.X[ranking],np.dot(self.Theta_x.T, self.W[user]))).shape))
                    # sys.stdout.flush()
                    # clicked_items_index = _clicks[i].nonzero()[0]
                    self.d[item] += Theta_v_W * (_clicks[i] - np.dot(self.X[ranking[i]],np.dot(self.Theta_x.T, self.W[user])))
                else:
                    self.d[item] += Theta_v_W * _clicks[i]
                self.V[item] = np.dot(self.CInv[item], self.d[item])
            self.XV[:, self.k:] = self.V

            self.n_samples[user] += len(_clicks)
            self.n_clicks[user] += sum(_clicks)

    def __collect_feedback(self, click, ranking):
        """
        :param y:
        :return: the last observed position.
        """
        # With  Cascade assumption, only the first click counts.
        if self.config.feedback_model == 'cascade':
            if np.sum(click) == 0:
                return click, ranking
            first_click = np.where(click)[0][0]
            return click[:first_click + 1], ranking[:first_click +1]
        elif self.config.feedback_model == 'dcm':
            if np.sum(click) == 0:
                return click, ranking
            last_click = np.where(click)[0][-1]
            return click[:last_click + 1], ranking[:last_click + 1]
        # all items are observed
        else:
            return click, ranking