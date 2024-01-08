#include <gtest/gtest.h>
#include <opencv2/opencv.hpp>

// cv::Matオブジェクトが等しいかどうかを確認する関数
bool AreMatEqual(const cv::Mat& mat1, const cv::Mat& mat2) {
    // 同じサイズとタイプであることを確認
    if (mat1.size() != mat2.size() || mat1.type() != mat2.type()) {
        return false;
    }
    // 要素ごとに比較
    return cv::countNonZero(mat1 != mat2) == 0;
}

// 'MatEquality' テストケース
TEST(MatEquality, TestMatEquality) {
    cv::Mat mat1 = (cv::Mat_<int>(2, 2) << 1, 2, 3, 4);
    cv::Mat mat2 = (cv::Mat_<int>(2, 2) << 1, 2, 3, 4);

    // AreMatEqual関数を使用してmat1とmat2が等しいかテスト
    EXPECT_TRUE(AreMatEqual(mat1, mat2));
}

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
