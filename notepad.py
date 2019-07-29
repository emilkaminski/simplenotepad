
class note(object):
    name = ""
    text = ""
    def __init__(self, name, text):
        self.name = name
        self.text = text
    def __str__(self):
        return self.name + ' - ' + self.text

class notepad(object):
    owner = ""
    notes = [] 
    def __init__(self, owner_name):
        self.owner = owner_name
    def add_note(self, note):
        self.notes.append(note)
    def remove_note(self, name):
        pass
    def __str__(self):
        txt = 'Zadania w notatniku ' + self.owner + '\n'
        for i in range(0,len(self.notes)):
            txt = txt + self.notes[i].name + ' - ' + self.notes[i].text + '\n'
        return txt

if __name__ == '__main__':

    n1 = note('zadanie', 'to jest zadanie do wykonania na jutro')
    n2 = note('pamiętać', 'kupić mleko w biedronce')

    nemil = notepad('Emil')
    nemil.add_note(n1)
    nemil.add_note(n2)
    print(nemil)
