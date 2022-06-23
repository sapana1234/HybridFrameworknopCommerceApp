import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    lnkCustomers_menuitem_xpath = "(//i[@class='nav-icon far fa-dot-circle'])[13]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = " //input[@id='Company']"
    txtcustomerRoles_xpath = "(//div[@role='listbox'])[2]"
    listitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    listitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    listitemGuests_xpath = "//li[contains(text(),'Guests')]"
    listitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_name = "save"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(8)

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItems(self):
        self.driver.implicitly_wait(8)
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Guests':
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuests_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.listitemAdministrators_xpath)
        elif role == 'Registered':
            self.driver.implicitly_wait(8)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.listitemRegistered_xpath)
        elif role == 'Guests':
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuests_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.listitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listitemRegistered_xpath)
            self.driver.implicitly_wait(8)
            # self.listitem.click()
            self.driver.execute_script("argument[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        self.driver.implicitly_wait(8)
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        time.sleep(3)
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        self.driver.implicitly_wait(8)
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        time.sleep(3)
        self.driver.find_element(By.NAME, self.btnSave_name).click()















