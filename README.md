#### How to use poetry to manage dependencies libraries    

[Poetry Article](https://blog.kyomind.tw/python-poetry/)    
[Poetry Offical Document](https://python-poetry.org/docs/#enable-tab-completion-for-bash-fish-or-zsh)

1. install 
```
curl -sSL https://install.python-poetry.org | python3 -

export PATH="/Users/james/.local/bin:$PATH"

```

2. virsual environment setting
```
    poetry config --list

    poetry config virtualenvs.in-project true

    poetry shell 
```

3. for new project to use poetry
```
    poetry init
    poetry env use python
    poetry shell
    poetry add or remove [lib]
```

4. [Debug](https://github.com/flet-dev/flet/pull/228)   
   Firstly, should use 'poetry shell' initialize virsual environment,        
   Then use 'flet src/main.py -d -r' to watch file chagne.    
```
 Image load picture: 
 add assets under src directory,
 Image(src=f"/images/your_pircture.png")
 then run
 flet run src/app.py -d -r --assets assets
```