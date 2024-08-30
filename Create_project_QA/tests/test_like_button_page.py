from Create_project_QA.pages.like_a_button import LikeAButtonPage


def test_button2_exist(browser):
    like_a_button = LikeAButtonPage(browser)
    like_a_button.open()
    assert like_a_button.button_is_displayed


def test_button2_clicked(browser):
    like_a_button = LikeAButtonPage(browser)
    like_a_button.open()
    like_a_button.click_button()
    assert 'Submitted' == like_a_button.result_text
