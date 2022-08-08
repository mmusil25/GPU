Email summarizer
================


Thank you [user:paravp](https://github.com/paravp) for your guidance


Have you ever received an obnoxiously long email from a coworker?
If you have access to email the answer is most likely yes. The
time investment required to process all of your coworkers' thoughts
is largely a waste of energy. Due to the onslaught of e-mails that
most people receive on a daily basis, an e-mail digest is required. 

This project guides the reader to create a .exe python GUI for email summarization.

Input(s): string, parameters 
Output(s): string

Methods
--------------------------------
The design pattern is model, view, controller

### controller.py

_Functions_
```
return void <-- run()
```

#### model.py

_Classes_

```
summarize
```

_Functions_

```
return sorted_output_sent <-- sort_sentences(self, original, output)
return sorted_output <-- get_summary(self, input, max_sentences)
```

#### view.py

_Functions_

```
return void <-- gui()
```


