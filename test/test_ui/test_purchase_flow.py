import allure
import pytest

from framework.utils import extract_price_as_decimal


@pytest.mark.ui
@allure.parent_suite("UI Tests")
@allure.suite("Checkout Flow")
@allure.feature("Purchase")
@allure.story("Complete checkout process")
class TestPurchaseFlow:

    @allure.title("Verify complete purchase flow from login to order confirmation")
    @allure.description(
        """
        This test verifies the complete purchase flow:
        1. User logs in
        2. Adds multiple products to cart
        3. Removes extra products leaving only one
        4. Proceeds to checkout
        5. Completes the purchase
        6. Verifies order confirmation
        """
    )
    def test_full_purchase_flow_with_item_removal_and_total_verification(
        self,
        product_in_cart,
        checkout_step_one_page,
        checkout_step_two_page,
        checkout_complete_page,
        fake_data,
    ):
        with allure.step("Open cart page with product"):
            cart_page, price_decimal = product_in_cart

        with allure.step("Click checkout button"):
            cart_page.click_checkout_button()

        first_name = fake_data.first_name()
        last_name = fake_data.last_name()
        postal_code = fake_data.postcode()

        with allure.step(f"Fill shipping information"):
            checkout_step_one_page.input_first_name_text(text=first_name)
            checkout_step_one_page.input_last_name_text(text=last_name)
            checkout_step_one_page.input_postal_code_text(text=postal_code)
            checkout_step_one_page.click_continue_button()

        with allure.step("Verify price details on summary page"):
            item_total_text = checkout_step_two_page.get_item_total_text()
            tax_text = checkout_step_two_page.get_tax_text()
            total_text = checkout_step_two_page.get_total_text()

            item_total_decimal = extract_price_as_decimal(item_total_text)
            tax_decimal = extract_price_as_decimal(tax_text)
            total_decimal = extract_price_as_decimal(total_text)

            allure.attach(
                f"Item total: {item_total_text}",
                name="Item Total",
                attachment_type=allure.attachment_type.TEXT,
            )
            allure.attach(
                f"Tax: {tax_text}",
                name="Tax",
                attachment_type=allure.attachment_type.TEXT,
            )
            allure.attach(
                f"Total: {total_text}",
                name="Total",
                attachment_type=allure.attachment_type.TEXT,
            )

            assert (
                price_decimal == item_total_decimal
            ), f"Price in cart doesn't match items total"

            expected_total = item_total_decimal + tax_decimal
            assert (
                total_decimal == expected_total
            ), f"Total amount doesn't match sum of items and tax"

        with allure.step("Complete checkout"):
            checkout_step_two_page.click_finish_button()

        with allure.step("Verify order completion"):
            complete_title = checkout_complete_page.get_title_text()
            complete_header = checkout_complete_page.get_complete_header_text()
            complete_text = checkout_complete_page.get_complete_text()

            allure.attach(
                complete_title,
                name="Completion Page Title",
                attachment_type=allure.attachment_type.TEXT,
            )
            allure.attach(
                complete_header,
                name="Completion Header",
                attachment_type=allure.attachment_type.TEXT,
            )
            allure.attach(
                complete_text,
                name="Completion Message",
                attachment_type=allure.attachment_type.TEXT,
            )

            assert complete_title == "Checkout: Complete!"
            assert complete_header == "Thank you for your order!"
            assert (
                complete_text
                == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
            )
