from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.text import LabelBase

LabelBase.register(name="acad_nusx_geo",
                   fn_regular="acad_nusx_geo.ttf"
                   )

Builder.load_file('rules.kv')


class MyLayout(Widget):
    arrUpToTwenty = ["i","erTi","ori","sami","oTxi","xuTi","eqvsi","Svidi","rva","cxra","aTi",
                     "TerTmeti","Tormeti","cameti","ToTxmeti","Txutmeti","Teqvsmeti", "Cvidmeti",
                     "Tvrameti", "Cxrameti", "oci"
                     ]
    arrHundreds = ["as","oras","samas","oTxas","xuTas",
                   "eqvsas", "Svidas", "rvaas","cxraas"
                   ]
    dozenNums = ["oc","oc","ormoc","ormoc","samoc","samoc","oTxmoc","oTxmoc"]
    andWord = "da"
    thousand = "aTasi"

    def showFunc(self):
        input = self.ids.number_input.text
        result = self.ids.result_num
        inputNum = int(input)
        answer = ""

        if input=="0":
            answer="nuli"
        elif input=="1000":
            answer="aTasi"
        if len(input)==3:
            if int(inputNum)%100 !=0:
                answer = self.arrHundreds[int(inputNum / 100) - 1] + " "
                input = str(inputNum % 100)
                inputNum = int(input)
            else:
                result.text = self.arrHundreds[int(inputNum / 100) - 1] + "i"
        if len(input)==1 or len(input)==2:
            if inputNum != 0:
                if inputNum < 21:
                    answer += self.arrUpToTwenty[inputNum]
                elif int(inputNum / 10) % 2 == 0:
                    if inputNum % 10 == 0:
                        answer += self.dozenNums[int(inputNum / 10) - 2] + self.arrUpToTwenty[int(inputNum % 10)]
                    else:
                        answer += self.dozenNums[int(inputNum / 10) - 2] + self.andWord + self.arrUpToTwenty[int(inputNum % 10)]
                else:
                    answer += self.dozenNums[int(inputNum / 10) - 2] + self.andWord + self.arrUpToTwenty[int(inputNum % 10) + 10]
            result.text = answer
class NumberDisplayerApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    NumberDisplayerApp().run()
