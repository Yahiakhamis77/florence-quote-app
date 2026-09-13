"""
Florence Travel Services - Quote Calculator (Android App)
============================================================
Built with Kivy so it compiles into a real installable Android app.

This file defines the app's screen and behavior. You don't need to
edit this - Claude maintains it. Just tell Claude what you want changed
and a new version will be provided.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.metrics import dp


class QuoteCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=dp(20), spacing=dp(10), **kwargs)

        self.add_widget(Label(
            text="Florence Travel Services",
            font_size="22sp",
            bold=True,
            size_hint_y=None,
            height=dp(50),
        ))
        self.add_widget(Label(
            text="Quote Calculator",
            font_size="16sp",
            size_hint_y=None,
            height=dp(30),
        ))

        form = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        form.bind(minimum_height=form.setter("height"))

        self.client_input = self._add_field(form, "Client name")
        self.flight_input = self._add_field(form, "Flight cost (USD)", numeric=True)
        self.hotel_input = self._add_field(form, "Hotel cost (USD)", numeric=True)
        self.rate_input = self._add_field(form, "USD -> LYD rate", numeric=True)

        self.add_widget(form)

        # Margin type toggle
        self.add_widget(Label(text="Margin type:", size_hint_y=None, height=dp(25)))
        margin_row = BoxLayout(size_hint_y=None, height=dp(45), spacing=dp(10))
        self.percent_btn = ToggleButton(text="Percentage", group="margin", state="down")
        self.flat_btn = ToggleButton(text="Flat amount", group="margin")
        margin_row.add_widget(self.percent_btn)
        margin_row.add_widget(self.flat_btn)
        self.add_widget(margin_row)

        self.margin_input = TextInput(
            hint_text="Margin value (e.g. 10 for 10%, or 50 for $50)",
            multiline=False,
            input_filter="float",
            size_hint_y=None,
            height=dp(45),
        )
        self.add_widget(self.margin_input)

        calc_btn = Button(
            text="Calculate Quote",
            size_hint_y=None,
            height=dp(55),
            background_color=(0.2, 0.5, 0.9, 1),
        )
        calc_btn.bind(on_press=self.calculate)
        self.add_widget(calc_btn)

        self.result_label = Label(
            text="",
            font_size="15sp",
            size_hint_y=None,
            halign="left",
            valign="top",
        )
        self.result_label.bind(texture_size=self.result_label.setter("size"))

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.result_label)
        self.add_widget(scroll)

    def _add_field(self, form, label_text, numeric=False):
        form.add_widget(Label(text=label_text, size_hint_y=None, height=dp(40)))
        field = TextInput(
            multiline=False,
            input_filter="float" if numeric else None,
            size_hint_y=None,
            height=dp(40),
        )
        form.add_widget(field)
        return field

    def calculate(self, instance):
        try:
            flight = float(self.flight_input.text or 0)
            hotel = float(self.hotel_input.text or 0)
            rate = float(self.rate_input.text or 0)
            margin_value = float(self.margin_input.text or 0)
        except ValueError:
            self._show_error("Please enter valid numbers in all cost fields.")
            return

        if rate <= 0:
            self._show_error("Please enter a valid exchange rate.")
            return

        subtotal = flight + hotel

        if self.percent_btn.state == "down":
            margin = subtotal * (margin_value / 100)
        else:
            margin = margin_value

        total_usd = subtotal + margin
        total_lyd = total_usd * rate

        client_name = self.client_input.text.strip()
        header = f"Client: {client_name}\n" if client_name else ""

        self.result_label.text = (
            f"{header}"
            f"Flight:          ${flight:,.2f}\n"
            f"Hotel:           ${hotel:,.2f}\n"
            f"Service margin:  ${margin:,.2f}\n"
            f"------------------------------\n"
            f"TOTAL (USD):     ${total_usd:,.2f}\n"
            f"TOTAL (LYD):     {total_lyd:,.2f} LYD"
        )

    def _show_error(self, message):
        popup = Popup(
            title="Missing info",
            content=Label(text=message),
            size_hint=(0.8, 0.3),
        )
        popup.open()


class QuoteApp(App):
    def build(self):
        return QuoteCalculator()


if __name__ == "__main__":
    QuoteApp().run()
