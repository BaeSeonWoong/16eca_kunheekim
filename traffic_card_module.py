# -*- coding: utf8 -*-

#[2013112007][김건희]







balance_won = 0


def deposit(amount):






    global balace_won


    balace_won += int(amount)


def pay(amount):






    global  balance_won





    def check():








        global balance_won
        return balance_won