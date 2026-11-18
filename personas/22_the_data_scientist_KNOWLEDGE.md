# 22_the_data_scientist_KNOWLEDGE.md
**Role:** Lead Data Scientist — Dr. Maya Lin
**Purpose:** Offline, high-density practitioner brief for Statistical Learning, Classification Algorithms, Regression Diagnostics, and Confusion Matrix Metrics.
**Primary Academic Anchors:** Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani (2021), *An Introduction to Statistical Learning* (ISLR, 2nd ed.); Aurélien Géron (2022), *Hands-On Machine Learning*; Provost & Fawcett (2013), *Data Science for Business*.

---

## 1. Classification Algorithms Overview (Image 1 Mathematical Grounding)

### A. Boosting (AdaBoost, Gradient Boosting, XGBoost, LightGBM)
*   **Theory:** Combines several weak learners sequentially, with each new model focusing on correcting the mistakes (residuals) made by previous models.
*   **Formulation:** Ensemble model $F_M(x) = \sum_{m=1}^M \gamma_m h_m(x)$.
*   **Gradient Boosting Mechanism:** At step $m$, compute pseudo-residuals $r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F=F_{m-1}}$, fit base learner $h_m(x)$ to $r_{im}$, and update $F_m(x) = F_{m-1}(x) + \eta \gamma_m h_m(x)$ where $\eta$ is the learning rate (shrinkage).
*   **Best Use:** Structured tabular datasets with non-linear relationships and interactions.

### B. Decision Trees (CART / C4.5)
*   **Theory:** Makes predictions by following a series of simple yes/no questions, recursively partitioning the feature space into rectangular regions.
*   **Splitting Criteria:**
    *   *Gini Impurity (CART default):* $G = 1 - \sum_{k=1}^K p_k^2$, where $p_k$ is the proportion of class $k$ in node.
    *   *Entropy / Information Gain:* $H = -\sum_{k=1}^K p_k \log_2(p_k)$.
*   **Pruning:** Cost-Complexity Pruning minimizes $R_\alpha(T) = R(T) + \alpha |T|$, balancing training error with tree complexity $|T|$.
*   **Strengths & Flaws:** Highly interpretable (white-box), but high variance and prone to severe overfitting if unpruned.

### C. K-Nearest Neighbors (KNN)
*   **Theory:** Instance-based, non-parametric algorithm that predicts the category most common among the $k$ most similar training examples in feature space.
*   **Distance Metrics:**
    *   *Euclidean ($L_2$):* $d(x, y) = \sqrt{\sum_{j=1}^p (x_j - y_j)^2}$
    *   *Manhattan ($L_1$):* $d(x, y) = \sum_{j=1}^p |x_j - y_j|$
    *   *Minkowski:* $d(x, y) = \left(\sum_{j=1}^p |x_j - y_j|^q\right)^{1/q}$
*   **Critical Operational Constraint:** Mandatory feature standardization ($z = \frac{x - \mu}{\sigma}$). Fails in high dimensions due to the **Curse of Dimensionality** (distance between points becomes uniform).

### D. Linear Discriminant Analysis (LDA)
*   **Theory:** Finds a linear combination of features that best separates two or more classes by maximizing between-class variance relative to within-class variance.
*   **Fisher's Criterion:** Maximizes $J(w) = \frac{w^T S_B w}{w^T S_W w}$, yielding optimal projection $w \propto S_W^{-1}(\mu_1 - \mu_2)$.
*   **Key Assumptions:** Features follow a multivariate normal distribution within each class, and all classes share a common covariance matrix $\Sigma$. If covariance matrices differ, use **Quadratic Discriminant Analysis (QDA)**.

### E. Naive Bayes (Gaussian, Multinomial, Bernoulli)
*   **Theory:** Computes posterior probability using Bayes' Theorem under the "naive" assumption of conditional feature independence given class $y$:
    $$P(y|x_1, \dots, x_p) \propto P(y) \prod_{j=1}^p P(x_j|y)$$
*   **Variants:**
    *   *Gaussian NB:* Continuous features modeled via normal distribution $\mathcal{N}(\mu_{yk}, \sigma_{yk}^2)$.
    *   *Multinomial NB:* Discrete word count frequencies for text classification with Laplace smoothing ($+\alpha$).
    *   *Bernoulli NB:* Binary indicator features (word presence/absence).
*   **Best Use:** High-dimensional sparse text data, rapid baseline modeling, sentiment classification.

### F. Neural Networks (Feedforward Multilayer Perceptron / MLP)
*   **Theory:** Learns hierarchical representations through layers of interconnected nodes (neurons) applying linear transformations followed by non-linear activations:
    $$a^{[l]} = g\left(W^{[l]} a^{[l-1]} + b^{[l]}\right)$$
*   **Activation Functions:** $\text{ReLU}(z) = \max(0, z)$, $\text{Sigmoid}(z) = \frac{1}{1 + e^{-z}}$, $\text{Softmax}(z)_i = \frac{e^{z_i}}{\sum e^{z_j}}$.
*   **Optimization:** Backpropagation computes gradients $\frac{\partial L}{\partial W^{[l]}}$ via the chain rule, optimized via Adam or RMSprop.

### G. Random Forest
*   **Theory:** Ensemble of decision trees trained with **Bagging (Bootstrap Aggregation)** and **Random Feature Subspace Sampling**.
*   **Mechanism:** Draws $B$ bootstrap samples. At each split, considers only $m \approx \sqrt{p}$ randomly selected features. Prediction is the majority vote (classification) or average (regression).
*   **Key Advantage:** Decorrelates individual trees, drastically reducing model variance without increasing bias. Provides built-in **Out-of-Bag (OOB)** error estimation without separate validation set.

### H. Support Vector Machine (SVM)
*   **Theory:** Finds the optimal hyperplane that separates categories with the maximum geometric margin while penalizing misclassifications.
*   **Soft Margin Objective:**
    $$\min_{w, b, \xi} \frac{1}{2}\|w\|^2 + C \sum_{i=1}^N \xi_i \quad \text{subject to } y_i(w^T x_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$
*   **The Kernel Trick:** Implicitly maps inputs to high-dimensional Hilbert space via Mercer kernel $K(x, z) = \langle \phi(x), \phi(z) \rangle$:
    *   *Linear:* $K(x, z) = x^T z$
    *   *RBF / Gaussian:* $K(x, z) = \exp(-\gamma \|x - z\|^2)$
    *   *Polynomial:* $K(x, z) = (\gamma x^T z + c)^d$

---

## 2. Confusion Matrix & Performance Metrics (Image 2 Mathematical Grounding)

### A. The Master Confusion Matrix Layout
$$\begin{array}{|c|c|c|}
\hline
& \textbf{Predicted Positive} & \textbf{Predicted Negative} \\
\hline
\textbf{Actual Positive} & \text{True Positive (TP)} & \text{False Negative (FN) [Type II Error]} \\
\hline
\textbf{Actual Negative} & \text{False Positive (FP) [Type I Error]} & \text{True Negative (TN)} \\
\hline
\end{array}$$

### B. Core Metric Formulas & Derivations
*   **Accuracy:** $\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$
    *   *Pitfall:* In a dataset with $99\%$ negative cases, a dummy classifier predicting all negative achieves $99\%$ accuracy while detecting 0 positives.
*   **Precision (Positive Predictive Value):** $\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$
    *   *Meaning:* Of all instances predicted as positive, what fraction was actually positive? Focus on Precision when the cost of False Positives is high (e.g. spam filters, loan fraud accusations).
*   **Recall / Sensitivity (True Positive Rate):** $\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$
    *   *Meaning:* Of all truly positive instances, what fraction did the model successfully find? Focus on Recall when the cost of False Negatives is catastrophic (e.g. cancer diagnosis, critical security breaches).
*   **Specificity (True Negative Rate):** $\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}$
*   **False Positive Rate (FPR):** $\text{FPR} = 1 - \text{Specificity} = \frac{\text{FP}}{\text{TN} + \text{FP}}$
*   **F1-Score (Harmonic Mean):**
    $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$
*   **$F_\beta$-Score:** Adjusts balance between Precision and Recall:
    $$F_\beta = (1 + \beta^2) \frac{\text{Precision} \times \text{Recall}}{\beta^2 \text{Precision} + \text{Recall}}$$
    ($\beta = 2$ weighs recall twice as heavily as precision; $\beta = 0.5$ weighs precision twice as heavily).
*   **ROC Curve (Receiver Operating Characteristic) & AUC:** Plots TPR (Recall) vs FPR across all probability thresholds $\tau \in [0, 1]$. An AUC of $0.5$ represents random guessing; $1.0$ represents a perfect classifier.
*   **Precision-Recall Curve (PR-AUC):** Plot of Precision vs. Recall. **Mandatory** standard over ROC-AUC when evaluating heavily imbalanced datasets (e.g. $<5\%$ positive class).

---

## 3. Regression Analysis & Validation (MGM Refresh Grounding)

### A. Ordinary Least Squares (OLS) Linear Regression
*   **Equation:** $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p + \epsilon$, where $\epsilon \sim \mathcal{N}(0, \sigma^2)$.
*   **Matrix Normal Equation:** $\hat{\beta} = (X^T X)^{-1} X^T y$.
*   **Core Assumptions (L-I-N-E):**
    1. *Linearity:* Relationship between predictors and target is linear.
    2. *Independence:* Residuals $\epsilon_i$ are independent (no autocorrelation; check Durbin-Watson statistic $\approx 2.0$).
    3. *Normality:* Residuals are normally distributed (Q-Q plot, Shapiro-Wilk test).
    4. *Equal Variance (Homoscedasticity):* Residual variance $\text{Var}(\epsilon_i)$ is constant across predicted values (Breusch-Pagan test; funnel shapes on residual plots indicate heteroscedasticity).
*   **Multicollinearity Diagnostics:** Variance Inflation Factor: $\text{VIF}_j = \frac{1}{1 - R_j^2}$. $\text{VIF} > 5$ indicates moderate multicollinearity; $\text{VIF} > 10$ requires feature removal or regularization.

### B. Regularization Frameworks
*   **Ridge Regression ($L_2$ Penalty):** Minimizes $\sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^p \beta_j^2$. Shrinks coefficients toward zero; robust to multicollinear predictors.
*   **Lasso Regression ($L_1$ Penalty):** Minimizes $\sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^p |\beta_j|$. Drives non-informative coefficients to exactly zero, producing sparse, interpretable models (automatic feature selection).
*   **ElasticNet:** Combines $L_1$ and $L_2$ penalties: $\lambda_1 \sum |\beta_j| + \lambda_2 \sum \beta_j^2$. Ideal when multiple features are correlated.

### C. Regression Performance Metrics
*   **Mean Squared Error (MSE):** $\text{MSE} = \frac{1}{n} \sum (y_i - \hat{y}_i)^2$ (penalizes large outlier errors heavily).
*   **Root Mean Squared Error (RMSE):** $\text{RMSE} = \sqrt{\text{MSE}}$ (interpretable in original units).
*   **Mean Absolute Error (MAE):** $\text{MAE} = \frac{1}{n} \sum |y_i - \hat{y}_i|$ (robust to extreme outliers).
*   **Coefficient of Determination ($R^2$):** $R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$. Fraction of target variance explained by predictors.
*   **Adjusted $R^2$:** $R_{\text{adj}}^2 = 1 - \frac{(1 - R^2)(n - 1)}{n - p - 1}$. Penalizes adding irrelevant predictors that do not improve explanatory power.
