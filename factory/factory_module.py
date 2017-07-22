# -*-coding:utf-8-*-
'''
Created on 2017年6月13日

@author: houguangdong
'''

import xml.etree.ElementTree as etree
import json


class A(object):
    pass


class JSONConnector():
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r') as f:
            self.data = json.load(f)
    
    @property
    def parsed_data(self):
        return self.data


class XMLConnector():
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)
    
    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print ve
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')
    xml_factory = connect_to('./person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print 'found: {} persons'.format(len(liars))
    for liar in liars:
        print 'first name: {}'.format(liar.find('firstName').text)
        print 'last name: {}'.format(liar.find('lastName').text)
        for p in liar.find('phoneNumbers'):
            print 'phone number {}'.format(p.attrib['type']), p.text
    
    json_factory = connect_to('./donut.json')
    json_data = json_factory.parsed_data
    print 'found {} donut'.format(len(json_data))
    for dount in json_data:
        print 'name: {}'.format(dount["name"])
        print 'price: {}'.format(dount["ppu"])
        for t in dount['topping']:
            print 'topping: {} {}'.format(t['id'], t['type'])


class Frog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def interact_with(self, obstacle):
        print "{} the Frog encounters {} and {}!".format(self, obstacle, obstacle.action())
    

class Bug:
    def __str__(self):
        return 'a bug'
    
    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print self
        self.player_name = name
    
    def __str__(self):
        return '\n\n\t----------Frog World---------'
    
    def make_character(self):
        return Frog(self.player_name)
    
    def make_obstacle(self):
        return Bug()
    

class Wizard:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
        
    def interact_with(self, obstacle):
        print "{} the Wizard battles against {} and {}!".format(self, obstacle, obstacle.action())
        

class Ork:
    def __str__(self):
        return "an evil ork"

    def action(self):
        return 'kills it'


class WizardWord:
    def __init__(self, name):
        print self
        self.play_name = name
    
    def __str__(self):
        return '\n\n\t-----------Wizard Word--------'
    
    def make_character(self):
        return Wizard(self.play_name)
    
    def make_obstacle(self):
        return Ork()
    

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    
    def play(self):
        self.hero.interact_with(self.obstacle)
    

def validate_age(name):
    try:
        age = raw_input("Welcome {}, how old are you".format(name))
        age = int(age)
    except ValueError as err:
        print "Age {} is invaild, please try again".format(age)
        return (False, age)
    return (True, age)


def main1():
    name = raw_input("Hello. What's your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWord
    environment = GameEnvironment(game(name))
    environment.play()
    
  
if __name__ == '__main__':
    a = A()
    b = A()
    print id(a) == id(b)
    print a, b
    main()
    main1()