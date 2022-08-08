import PySimpleGUI as g, controller

g.theme('Light Brown 3')

ip_size = (80,40)
opt_size = (20,5)

lo = [
    [g.Text('Paste email')],
    [g.Input(key='-IP-', size=ip_size)],
    [g.Text('Choose options')],
    [g.Input(key='-NSNTC-', size=opt_size)],
    [g.Button('Click to summarize')],
    [g.Output(size=ip_size)]
]

win = g.Window('Email summarizer',lo)
while 1:
    evnt, vls = win.read()
    if evnt == 'Close' | None:
        break
    elif evnt == 'Input' | 'Click to summarize':
        email_summary = controller.go(vls['-IP-'])



