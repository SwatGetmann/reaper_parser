from tokenizer import tokenize_node

test_text = """<MYTAG "Hello There!" v0.1 ""
  SOME_INFO 0 -1 4.672 "" 2.9183
  <TRACK
    POS x y
  >
  <TRACK
    POS 2.6 1.5
    <ITEM
      NAME "Wonderful Stuff"
    >
    <AUTOMAT 0 "" "" -1
      JOIN LEFT
    >
  >
  <TRACK
    POS 1.4 8.8
    NAME "Something Draft"
  >
>"""

heads = tokenize_node(test_text.split("\n"), supress_output=False)
print(heads[0])
heads[0].print_tree()
