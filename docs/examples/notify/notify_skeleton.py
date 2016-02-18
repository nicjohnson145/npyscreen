import npyscreen


class NotifyWaitExample(npyscreen.Form):
    def create(self):
        key_of_choice = 'p'
        what_to_display = 'Press {} for popup \n Press escape key to quit'.format(key_of_choice)

        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application
        self.display_text = self.add(npyscreen.FixedText, value=what_to_display, height=2)

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False


class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', NotifyWaitExample, name='To show off notify_wait')


if __name__ == '__main__':
    TestApp = MyApplication().run()