def KeywordTest1():
    #Runs the "Orders" tested application.
    TestedApps.Orders.Run(1, True)
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Clicks the 'Group' object.
    Aliases.Orders.OrderForm.Group.Click(122, 157)
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(24, 11)
    #Enters '[Caps]' in the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Keys("[Caps]")
    #Enters the text 'S' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("S")
    #Enters '[Caps]' in the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Keys("[Caps]")
    #Enters the text 'Soniua' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("Soniua")
    #Clicks the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Click(25, 5)
    #Enters the text 'str1' in the 'Street' text editor.
    Aliases.Orders.OrderForm.Group.Street.SetText("str1")
    #Clicks the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Click(21, 5)
    #Enters the text 'hyd' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("hyd")
    #Clicks the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Click(81, 6)
    #Enters '[Caps]' in the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Keys("[Caps]")
    #Enters the text 'A' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("A")
    #Enters '[Caps]' in the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Keys("[Caps]")
    #Enters the text 'Ap' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("Ap")
    #Clicks the 'Zip' object.
    Aliases.Orders.OrderForm.Group.Zip.Click(24, 9)
    #Enters the text '5443565' in the 'Zip' text editor.
    Aliases.Orders.OrderForm.Group.Zip.SetText("5443565")
    #Clicks the 'CardNo' object.
    Aliases.Orders.OrderForm.Group.CardNo.Click(158, 10)
    #Enters the text '638783765' in the 'CardNo' text editor.
    Aliases.Orders.OrderForm.Group.CardNo.SetText("638783765")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|Edit order...")
    #Clicks the 'ButtonCancel' button.
    Aliases.Orders.OrderForm.ButtonCancel.ClickButton()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(60, 5)
    #Enters '![ReleaseLast]' in the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Keys("![ReleaseLast]")
    #Enters the text 'puy' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("puy")
    #Clicks the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Click(54, 12)
    #Enters the text 'Str2' in the 'Street' text editor.
    Aliases.Orders.OrderForm.Group.Street.SetText("Str2")
    #Clicks the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Click(21, 12)
    #Enters the text 'htpg' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("htpg")
    #Clicks the 'Zip' object.
    Aliases.Orders.OrderForm.Group.Zip.Click(6, 6)
    #Enters the text '6547' in the 'Zip' text editor.
    Aliases.Orders.OrderForm.Group.Zip.SetText("6547")
    #Clicks the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Click(102, 9)
    #Enters the text 'Ap' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("Ap")
    #Clicks the 'CardNo' object.
    Aliases.Orders.OrderForm.Group.CardNo.Click(137, 2)
    #Enters the text '865678' in the 'CardNo' text editor.
    Aliases.Orders.OrderForm.Group.CardNo.SetText("865678")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Clicks the 'MyMoney' subitem of the 'puy' item of the 'OrdersView' list view.
    Aliases.Orders.MainForm.OrdersView.ClickItem("puy", "MyMoney")
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|Edit order...")
    #Selects the 'ScreenSaver' item of the 'ProductNames' combo box.
    Aliases.Orders.OrderForm.Group.ProductNames.ClickItem("ScreenSaver")
    #Clicks the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Click(30, 6)
    #Enters the text 'tpg' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("tpg")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Clicks the 'MyMoney' subitem of the 'Soniua' item of the 'OrdersView' list view.
    Aliases.Orders.MainForm.OrdersView.ClickItem("Soniua", "MyMoney")
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|Delete order")
    #Clicks the 'btnYes' button.
    Aliases.Orders.dlgConfirmation.btnYes.ClickButton()
    #Closes the 'MainForm' window.
    Aliases.Orders.MainForm.Close()
    #Clicks the 'btnNo' button.
    Aliases.Orders.dlgConfirmation.btnNo.ClickButton()     
