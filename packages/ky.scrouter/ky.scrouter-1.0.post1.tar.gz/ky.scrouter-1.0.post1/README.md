# Scrouter

A tool that looks for relations between users.

## Installing

Via pip:

```
pip install ky.scrouter
```

You can also update to the latest version:

```
pip install ky.scrouter --upgrade
```

**Make sure you have Python 3.8 or above installed!**

## Program launch

Via terminal:

```
python -m scrouter
```

After that, program will try to find the shortest follower of follower path:

![](https://gyazo.com/c7525a054da578cfb09395093afb1e51.png)

## Library

```python
>>> import scrouter
>>> scrouter.route('user1', 'user2')
...
```

## License
This project follows MIT license (see [LICENSE](LICENSE)).
