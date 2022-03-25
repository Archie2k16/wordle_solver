a python implementation of the famous WORDLE game

---

### how to use

+ play the wordle game in command line
```bash
python wordle.py
```
<style>
.emu{
    background-color:#333;
    color:#fff;
    padding:20px;
}
.r{
    color:#f00
}
.g{
    color:#0f0
}
.y{
    color:#ff0
}
</style>
<div class="emu">
<p>1: give a guess:</p>
<p>menes</p>
<p>ABCD<span class="r">E</span>FGHIJKL<span class="y">M</span><span class="r">N</span>OPQR<span class="g">S</span>TUVWXYZ</p>
<p><span class="y">M</span>ENE<span class="g">S</span></p>
<p>2: give a guess:</p>
<p>whams</p>
<p><span class="r">A</span>BCD<span class="r">E</span>FG<span class="y">H</span>IJKL<span class="y">M</span><span class="r">N</span>OPQR<span class="g">S</span>TUV<span class="r">W</span>XYZ</p>
<p>WH<span class="y">AM</span><span class="g">S</span></p>
<p>3: give a guess:</p>
<p>homos</p>
<p><span class="r">A</span>BCD<span class="r">E</span>FG<span class="g">H</span>IJKL<span class="g">M</span><span class="r">N</span><span class="g">O</span>PQR<span class="g">S</span>TUV<span class="r">W</span>XYZ</p>
<p class='g'>HOMOS</p>
<p>Correct! the wordle is "HOMOS"</p>
</div>

+ generate a random wordle 

```python
from wordle import Wordle

my_wordle = Wordle()

my_wordle.guess('xxxxx') # guess with a user defined answer

```