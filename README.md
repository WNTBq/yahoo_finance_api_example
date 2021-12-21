# Step by step installation mit virtueller Python-Umgebung:


1.) Der folgende Befehl "git clone" erstellt einen neuen Ordner mit den Projekt im akutellen Verzeichnis
```
% git clone https://github.com/WNTBq/yahoo_finance_api_example.git
Cloning into 'yahoo_finance_api_example'...
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 13 (delta 2), reused 9 (delta 1), pack-reused 0
Receiving objects: 100% (13/13), done.
Resolving deltas: 100% (2/2), done.
```
2.) in das Verzeichnis wechseln
```
% cd yahoo_finance_api_example 
```
3.) Virtuelle Python Umgebung im Ordner erstellen  
a) Ordner "env" erstellen
```
% mkdir env
```
b) virtuelle umgebung erstellen (in "env") 
```
% python3 -m venv env
```
c) virtuelle Umgebung aktivieren
```
% source env/bin/activate
```
d) Abhängigkeiten/Requirements installieren
```
% pip install -r requirements.txt
```
# Achtung:  
In der Console steht am Anfang des Command-Prompt "(env)", dies informiert darüber das die virtuelle Python-Umgebung aktiviert ist.
Das ausführen der Beispiele sollte dann über die Console funktionieren:
```
% python3 4_example_plotly.py 
```
In "Visual Studio Code" muss man evt. noch diese Virtuelle-Umgebung auswählen (links unten) indem man den relativen Pfad angibt:
```
./env/bin/python
```
(der Pfad relative zum root-Verzeichnis des VS Code Projekts)



