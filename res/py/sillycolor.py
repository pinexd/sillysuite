from pyscript import document

def process_script(event):
            # Find Values
            color_val = document.querySelector("#color").value
            msg_val = document.querySelector("#msg").value
            container = document.querySelector("#outputContainer")
            output = document.querySelector("#output")
            
            
            # Output Formatting
            result = f"[color={color_val}]{msg_val}[/color]"
            
            # Actually output
            output.innerText = result

            # make container visible
            if container:
                    container.style.display = "block"