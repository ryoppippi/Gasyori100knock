#include <gtest/gtest.h>
#include <opencv2/opencv.hpp>

// cv::Mat�I�u�W�F�N�g�����������ǂ������m�F����֐�
bool AreMatEqual(const cv::Mat& mat1, const cv::Mat& mat2) {
    // �����T�C�Y�ƃ^�C�v�ł��邱�Ƃ��m�F
    if (mat1.size() != mat2.size() || mat1.type() != mat2.type()) {
        return false;
    }
    // �v�f���Ƃɔ�r
    return cv::countNonZero(mat1 != mat2) == 0;
}

// 'MatEquality' �e�X�g�P�[�X
TEST(MatEquality, TestMatEquality) {
    cv::Mat mat1 = (cv::Mat_<int>(2, 2) << 1, 2, 3, 4);
    cv::Mat mat2 = (cv::Mat_<int>(2, 2) << 1, 2, 3, 4);

    // AreMatEqual�֐����g�p����mat1��mat2�����������e�X�g
    EXPECT_TRUE(AreMatEqual(mat1, mat2));
}

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
