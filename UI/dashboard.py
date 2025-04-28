def apply_stylesheet(self, stylesheet):
        self.dashboard.setStyleSheet(stylesheet)
        self.applicants.setStyleSheet(stylesheet)
        self.jobmanagent.setStyleSheet(stylesheet)
        self.history.setStyleSheet(stylesheet)
        self.satsana.setStyleSheet(stylesheet)
        self.account.setStyleSheet(stylesheet)
        self.pushButton.setStyleSheet(stylesheet)
        self.pushButton_2.setStyleSheet(stylesheet)
        self.pushButton_3.setStyleSheet(stylesheet)
        
    def toggleButtonStyle(self, button, button_name):
        # Reset the style of the previously clicked button
        for key in self.button_states:
            if key != button_name and self.button_states[key]:
                getattr(self, key).setStyleSheet("border: none; border-radius: 5px; padding: 10px; background-color: rgb(226, 249, 255);")
                self.button_states[key] = False

        # Apply the pressed style to the current button
        if self.button_states[button_name]:  # If the button is already pressed
            button.setStyleSheet("border: none; border-radius: 5px; padding: 10px; background-color: rgb(226, 249, 255);")
            self.button_states[button_name] = False
        else:
            button.setStyleSheet("background-color: white; border: 3px solid #F1F2F2; border-radius: 5px; padding: 10px;")
            self.button_states[button_name] = True
