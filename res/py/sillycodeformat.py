from pyscript import document

def process_script(event):
            # Find Values
            msg_val = document.querySelector("#msg").value
            container = document.querySelector("#outputContainer")
            output = document.querySelector("#output")
            helpme = ["#boldF", "#italic", "#underline", "#strikethrough", "#url"]
            formats = []
            
            #make sure backslashes don't blow everything up
            if "\\" not in msg_val:
                    msg_val_formatted = msg_val
            else:
                    msg_val.replace('\\', '\\\\')

            #create formats list
            def update_checkboxes():
                    formats.clear()
                    for boxes in helpme:
                            add = document.querySelector(boxes).checked
                            formats.append(add)
            update_checkboxes()

            for i, format in enumerate(formats):
                #there's probably a better way to do this
                if i == 0:
                    result = msg_val_formatted
                    if format == True:
                        result = "[b]" + msg_val_formatted + "[/b]"
                if i == 1:
                    if format == True:
                        result = "[i]" + result + "[/i]"
                if i == 2:
                    if format == True:
                        result = "[u]" + result + "[/u]"
                if i == 3:
                    if format == True:
                        result = "[s]" + result + "[/s]"
                if i == 4:
                    if format == True:
                        result = "[url]" + result + "[/url]"

            output.innerText = result

            # make container visible
            if container:
                    container.style.display = "block"