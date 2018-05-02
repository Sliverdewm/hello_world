import sys                         #导入sys模块

Zero=["  ***   ",
      " *   *  ",
      "*     * ",
      "*     * ",
      "*     * ",
      " *   *  ",
      "  ***   "]

One= ["  *   ",
      " **   ",
      "  *   ",
      "  *   ",
      "  *   ",
      "  *   ",
      " ***  "]
Two =["  ***  ",
      " *   * ",
      " *  *  ",
      "   *   ",
      "  *    ",
      " *     ",
      " ***** "]
Three=[" ***  ",
       "*   * ",
       "    * ",
       " **   ",
       "    * ",
       "*   * ",
       " ***  "]
Four=["     *  ",
      "   * *  ",
      "  *  *  ",
      " *   *  ",
      "******* ",
      "     *  ",
      "     *  "]
Five=["  ***** ",
      "  *     ",
      "  ****  ",
      "      * ",
      "       *",
      " *    * ",
      "  ****  "]

Six=["   ****   ",
     "  *    *  ",
     "  *       ",
     "  * ***   ",
     "  *    *  ",
     "  *    *  ",
     "   ****   "]
Seven=[" ******* ",
       "       * ",
       "      *  ",
       "     *   ",
       "    *    ",
       "   *     ",
       "   *     "]
Eight=["   ****   ",
       "  *    *  ",
       "  *    *  ",
       "  * ** *  ",
       "  *    *  ",
       "  *    *  ",
       "   ****   "]
Nine= ["   ****   ",
       "  *    *  ",
       "  *    *  ",
       "  * ** *  ",
       "       *  ",
       "       *  ",
       "   ****   "]

Dights=[Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]

try:
    dights=sys.argv[1]            #sys.argv[]其实是一个列表，里面的项是用户从界面输入，关键就是要明白这参数是从程序外部输入的，
                                    而非代码本身的什么地方，要想看到它的效果就应该将程序保存了，从外部来运行程序并给出参数。
   
   row=0
    while row<7:
        line=""
        column=0
        while column <len(dights):
            number=int(dights[column])
            digit=Dights[number]
            line += digit[row] + " "
            column+=1
        print(line)
        row+=1
except IndexError:
    print("usage:bigdigts.by<numbeer>")
except ValueError as err:
    print(err,"in",digits)
  
