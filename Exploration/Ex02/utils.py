import os
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV


def rmse(y, y_pred):
    return np.sqrt(mean_squared_error(np.expm1(y), np.expm1(y_pred)))


def get_scores(models, X, y):
    df = {}

    for model in models:
        model_name = model.__class__.__name__

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        df[model_name] = rmse(y_test, y_pred)
        score_df = pd.DataFrame(df, index=["RMSE"]).T.sort_values(
            "RMSE", ascending=False
        )

    return score_df


def grid_search_cv(model, train, y, param_grid, verbose=2, n_jobs=5):
    # GridSearchCV 모델로 초기화
    grid_model = GridSearchCV(
        model,
        param_grid=param_grid,
        scoring="neg_mean_squared_error",
        cv=5,
        verbose=verbose,
        n_jobs=n_jobs,
    )

    # 모델 fitting
    grid_model.fit(train, y)

    # 결과값 저장
    params = grid_model.cv_results_["params"]
    score = grid_model.cv_results_["mean_test_score"]

    # 데이터 프레임 생성
    results = pd.DataFrame(params)
    results["score"] = score

    # RMSLE 값 계산 후 정렬
    results["RMSLE"] = np.sqrt(-1 * results["score"])
    results = results.sort_values("RMSLE")

    return results


def save_submission(model, train, y, test, model_name, rmsle=None):
    model.fit(train, y)
    prediction = model.predict(test)
    prediction = np.expm1(prediction)
    data_dir = "/Users/masang/Desktop/aiffel/AIFFEL_quest_rs/Exploration/Ex02/data"
    submission_path = os.path.join(data_dir, "sample_submission.csv")
    submission = pd.read_csv(submission_path)
    submission["price"] = prediction
    submission_csv_path = "{}/submission_{}_RMSLE_{}.csv".format(
        data_dir, model_name, rmsle
    )
    submission.to_csv(submission_csv_path, index=False)
    print("{} saved!".format(submission_csv_path))
