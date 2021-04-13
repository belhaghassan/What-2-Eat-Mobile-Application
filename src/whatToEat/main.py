from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from Meals import *

import random
import time

meal = "lunch"
sm = ScreenManager()

Window.size = (350, 600)

''' -------------------- SCREEN CLASSES -------------------- '''


class StartScreen(Screen):
    pass


class Option1Screen(Screen):
    pass


class Option2Screen(Screen):
    pass


class Option3Screen(Screen):
    pass


class Option4Screen(Screen):
    pass


class DecisionScreen(Screen):
    selection = StringProperty()


class ThemeScreen(Screen):
    pass


class MealTypeScreen(Screen):
    pass


''' ----------------- END OF SCREEN CLASSES ----------------- '''


class User:
    default = "undecided"
    question1 = default
    question2 = default
    question3 = default
    question4 = default
    question5 = default


user1 = User()


class What2EatApp(MDApp):
    foodDecision = "Blank"
    matchedFoods = []  # Array to store the matched foods
    index = 0

    def light_theme(self):
        self.theme_cls.theme_style = "Light"

    def dark_theme(self):
        self.theme_cls.theme_style = "Dark"

    def meal_breakfast(self):
        global meal
        meal = "breakfast"

    def meal_lunch(self):
        global meal
        meal = "lunch"

    def meal_dinner(self):
        global meal
        meal = "dinner"

    # Functions for Option1Screen
    def dining_press(self):  # If Dining Out is selected, set question 1 to "dining"
        user1.question1 = "dining out"

    def cooking_press(self):  # If Cooking at Home is selected, set question 1 to "cooking"
        user1.question1 = "cook at home"

    def opt1_rand(self):  # If Choose For Me is selected, randomly set question 1 value
        num = random.randint(0, 1)
        if num == 0:
            user1.question1 = "dining out"
        else:
            user1.question1 = "cook at home"

    # Functions for Option2Screen
    def sweet_press(self):  # If Sweet is selected, set question 2 to "sweet"
        user1.question2 = "sweet"

    def salty_press(self):  # If Salty is selected, set question 2 to "salty"
        user1.question2 = "salty"

    def opt2_rand(self):  # If Choose For Me is selected, randomly set question 2 value
        num = random.randint(0, 1)
        if num == 0:
            user1.question2 = "sweet"
        else:
            user1.question2 = "salty"

    # Functions for Option3Screen
    def healthy_press(self):  # If Healthy is selected, set question 3 to "healthy"
        user1.question3 = "healthy"

    def casual_press(self):  # If Casual is selected, set question 3 to "casual"
        user1.question3 = "casual"

    def opt3_rand(self):  # If Choose For Me is selected, randomly set question 3 value
        num = random.randint(0, 1)
        if num == 0:
            user1.question3 = "healthy"
        else:
            user1.question3 = "casual"

    # Functions for Option4Screen
    def light_press(self):  # If Light is selected, set question 4 to "light"
        user1.question4 = "light"

    def heavy_press(self):  # If Heavy is selected, set question4 to "heavy"
        user1.question4 = "heavy"

    def opt4_rand(self):  # If Choose For Me is selected, randomly set question 4 value
        num = random.randint(0, 1)
        if num == 0:
            user1.question4 = "light"
        else:
            user1.question4 = "heavy"

    def idk_rand(self):  # If "I Don't Know" is selected, randomly assign all answers
        num = random.randint(0, 1)
        if num == 0:
            user1.question1 = "dining out"
        else:
            user1.question1 = "cook at home"
        num = random.randint(0, 1)
        if num == 0:
            user1.question2 = "sweet"
        else:
            user1.question2 = "salty"
        num = random.randint(0, 1)
        if num == 0:
            user1.question3 = "healthy"
        else:
            user1.question3 = "casual"
        num = random.randint(0, 1)
        if num == 0:
            user1.question4 = "light"
        else:
            user1.question4 = "heavy"

    # Function used to match the users selections to the food database
    # If the users selection matches a Fooditem, that food gets moved to a matched food list
    # A random food from the matched food list is selected and presented to the user
    def user_answers(self, matchedFoodsAmount=0):
        print(user1.question1 + ", ",
              user1.question2 + ", ",
              user1.question3 + ", ",
              user1.question4 + ", ",
              user1.question5 + ", ",
              meal)

        for obj in foodList:
            if (user1.question1 == obj.dining) & (meal == obj.mealType):
                if user1.question2 == obj.flavor1:
                    obj.attribute += 1
                if user1.question3 == obj.health:
                    obj.attribute += 1
                if user1.question4 == obj.weight:
                    obj.attribute += 1
                if obj.attribute >= 2:
                    self.matchedFoods.append(obj)
                    matchedFoodsAmount += 1

        self.matchedFoods.sort()
        self.foodDecision = self.matchedFoods[0].itemName

        for item in self.matchedFoods:  # to test the matchedFoods
            print(item.itemName)
            # self.foodDecision = item.itemName

    def next_suggestion(self):
        if self.foodDecision == self.matchedFoods[self.index].itemName or \
                self.foodDecision == self.matchedFoods[self.index - 1].itemName:
            self.foodDecision = self.matchedFoods[self.index].itemName
            self.index += 1


    # JUNK Terminal Testing (DELETE LATER)
    def showFood(self):
        print(self.foodDecision)

    # Used to update displayed food suggestions (Swipe-like feature)
    def new_decision(self):
        name = str(time.time())
        selection = self.foodDecision

        s = DecisionScreen(name=name)
        s.selection = selection
        sm.add_widget(s)
        sm.current = name

    def build(self):
        # Create the screen manager
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(Option1Screen(name='option1'))
        sm.add_widget(Option2Screen(name='option2'))
        sm.add_widget(Option3Screen(name='option3'))
        sm.add_widget(Option4Screen(name='option4'))
        sm.add_widget(DecisionScreen(name='decision'))
        sm.add_widget(ThemeScreen(name='theme'))
        sm.add_widget(MealTypeScreen(name='mealType'))

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"

        return sm


What2EatApp().run()
