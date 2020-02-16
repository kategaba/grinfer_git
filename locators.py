from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//div[text()='Sign in']")
    EMAIL = (By.CSS_SELECTOR, "#form_email")
    PASSWORD = (By.CSS_SELECTOR, "#form_password")
    LOG_BUTTON = (By.XPATH, "//button[@type='submit']")
    REG_LINK = (By.XPATH, "//span[text()='Sign up']/..")
    WELCOME_TEXT = (By.XPATH, "//div[text()='Welcome on board']")
    USER_LOGIN_TEXT = (By.XPATH, "//div[text()='Become an Author']")
    SEARCH_BUTTON = (By.XPATH, "//input[@class='ant-input']")
    COOKIE = (By.XPATH, "//span[text()='I agree']/..")
    REG_EMAIL = (By.CSS_SELECTOR, "#form_email")
    FIRST_NAME = (By.CSS_SELECTOR, "#form_firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#form_lastName")
    REG_PASSWORD = (By.CSS_SELECTOR, "#form_password")
    AGREE = (By.CSS_SELECTOR, "#form_agreement.ant-checkbox-input")
    REG_BUTTON = (By.XPATH, "//button[@type='submit']")
    TOGGLER = (By.XPATH, "//div[text()='Become an Author']")
    UPLOAD_AUTHOR_PHOTO = (By.XPATH, "//input[@type='file']")
    TOPIC = (By.CSS_SELECTOR, "#form_topics")
    #SELECTED_TOPIC = (By.XPATH, "//li[@role='option']")
    SELECTED_TOPIC = (By.XPATH, "//li[text()='Academics & Languages']")
    SUBTOPIC = (By.CSS_SELECTOR, "#form_subTopicIds")
    SELECTED_SUBTOPIC = (By.XPATH, "//li[text()='Academics']")
    BECOME_AUTHOR = (By.XPATH, "//div[text()='Become an Author']/.")
    JOB_TITLE = (By.CSS_SELECTOR, "#form_title")
    NEXT = (By.XPATH, "//span[text()='Next']/..")
    AGREE_AUTHOR = (By.CSS_SELECTOR, ".ant-checkbox-input")
    COMPLETE = (By.XPATH, "//span[text()='Complete']/..")
    AVATAR_BUTTON_MENU = (By.XPATH, "//span[contains(@class, 'ant-avatar')]/..")
    SIGN_OUT = (By.XPATH, "//div[text()='Sign Out']")
    CLEAR_CACHE = (By.XPATH, "//*[@id='clearBrowsingDataConfirm']")
    POPUP_LOGIN = (By.XPATH, "//span[@class='ant-notification-notice-message-single-line-auto-margin']/..")

class CoursePageLocators():
    COURSES = (By.XPATH, "//div[text()='Courses']")
    CREATE_NEW_COURSE = (By.XPATH, "//div[text()='Create a new course']/..")
    DOTS_MENU = (By.XPATH, "//div[@data-autotest='dots-course-menu']")
    EDIT_DRAFT = (By.XPATH, "//div[text()='Edit draft']/..")
    LANGUAGE = (By.XPATH, "//div[@data-qa-description='select-language-input']")
    SELECT_LANGUAGE = (By.XPATH, "//div[text()='English']")
    TOPIC = (By.XPATH, "//div[@data-qa-description='source-topic-select-input']")
    SELECTED_TOPIC = (By.XPATH, "//div[text()='Beauty']")
    SUBTOPIC = (By.XPATH, "//div[@data-qa-description='source-topic-sub-select-input']")
    SELECTED_SUBTOPIC = (By.XPATH, "//div[text()='Cosmetics']")
    UPLOAD_COURSE_COVER = (By.XPATH, "//div[@data-qa-description='course-cover-file-upload-button']/..")
    UPLOAD_FROM_HARD_DRIVE = (By.XPATH, "//input[@type='file']")
    CLOSE_NOTIFICATION = (By.CSS_SELECTOR, "span.ant-notification-notice-btn > a")
    SELECT_FILE_BUTTON = (By.XPATH, "//div[text()='Select files on Grinfer System']/..")
    SELECT_FILE = (By.XPATH, "//input[@type='radio']/..")
    COMPLETE = (By.XPATH, "//span[text()='Complete']/..")
    COURSE_TITLE = (By.XPATH, "//div[@data-qa-description='descriptive-course-title']/div[@class='DraftEditor-root']/div/div")
    COURSE_DESCRIPTION = (By.XPATH, "//div[@data-qa-description='descriptive-course-description']/div[@class='DraftEditor-root']/div/div")
    UPLOAD_WELCOME = (By.XPATH, "//div[@data-qa-description='course-media-file-upload-button']/..")
    COURSE_PRICE = (By.XPATH, "//div[@data-qa-description='undefinedundefinedprice-tier-select-input']/..")
    SELECT_PRICE = (By.XPATH, "//div[text()='Tier 1']/..")
    NEXT = (By.XPATH, "//span[text()='Next, create lesson']/..")
    CREATE_NEW_LESSON = (By.XPATH, "//div[text()='Create a new lesson']/..")
    LESSON_TITLE = (By.XPATH, "//div[@data-qa-description='lesson-title']/div[@class='DraftEditor-root']/div/div")
    LESSON_DESCRIPTION = (By.XPATH, "//div[@data-qa-description='lesson-description']/div[@class='DraftEditor-root']/div/div")
    LESSON_CONTENT = (By.XPATH, "//div[@data-qa-description='lesson-content-section']/div[@class='DraftEditor-root']/div/div")
    ADD_BUTTON = (By.CSS_SELECTOR, '#add-button')
    ADD_IMAGE = (By.XPATH, "//button[@title='Add an Image']")
    EDIT_COURSE_COVER = (By.XPATH, "//div[@data-qa-description='course-cover-file-upload-button']")
    EDIT_WELCOME = (By.XPATH, "//div[@data-qa-description='course-media-file-upload-button']")
    CREATE_LESSON_BUTTON = (By.XPATH, "//span[text()='Create lesson']/..")
    SAVE_DRAFT = (By.XPATH, "//span[text()='Save as draft']/..")
    COURSE_LESSON = (By.XPATH, "//li[text()='Course lessons']")
    EDIT_LESSON = (By.XPATH, "//div[text()='Edit']/..")
    SAVE_LESSON_BUTTON = (By.XPATH, "//span[text()='Save lesson']/..")
    DELETE_DRAFT = (By.XPATH, "//div[text()='Delete draft']/..")
    DELETE_CONFIRM = (By.XPATH, "//span[text()='Delete course']/..")
    BACK_BUTTON = (By.XPATH, "//button[@data-qa-description='back-button']/..")
    DELETE_LESSON_BUTTON = (By.XPATH, "//span[text()='Delete Lesson']/..")
    DELETE_LESSON_CONFIRM = (By.XPATH, "//span[text()='Yes, delete']/..")
    PUBLISH_COURSE = (By.XPATH, "//span[text()='Publish Course']/..")
    SEND_TO_MODERATION = (By.XPATH, "//span[text()='Send']/..")
    COURSE_TILE = (By.XPATH, "//div[contains(text(), 'Test course')]/..")
    APPROVE = (By.XPATH, "//span[text()='Approve']/..")
    MODERATOR_CONFIRM = (By.XPATH, "//span[text()='Confirm']/..")
    DECLINE = (By.XPATH, "//span[text()='Decline']/..")
    COMMENT = (By.XPATH, "//textarea[@placeholder='Enter your comment']")
    DELETE_COURSE = (By.XPATH, "//div[text()='Delete course']/..")