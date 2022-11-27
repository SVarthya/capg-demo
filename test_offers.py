from POM.offers import Offers_module

class Test_offers:
    def test_offers(self, _driver):
        offers = Offers_module(_driver)
        offers.holidays()
        offers.button_Holidays()
        offers.button_Holidays_offer()
        offers.Holidays_booknow_button()
        offers.Holidays_skip1()
        offers.Holidays_skip2()
        offers.Holidays_skip3()
        offers.Holidays_skip4()
        offers.Holidays_close()
        offers.trains()
        offers.trains_Offer()
        offers.trains_booknow_button()

