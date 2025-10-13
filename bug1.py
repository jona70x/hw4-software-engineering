# class Base:
# TODO: there's code missing in one or more lines below

class Circle():
    def __init__(x, size):
        super().__init__(x, y, size)

    def draw(self):
        return f"""
    ({self.x}, {self.y})\n{self.size}
                , - ~ ~ ~ - ,
            , '               ' ,
           ,                     ,
          ,                       ,
         ,                         ,
         ,                         ,
         ,                         ,
          ,                       ,
           ,                      ,
             ,                 , '
               ' - , _ _ _ , '
                        """
    
# def main():
#     c = Circle(1,2,3)
#     print(c.shape())
#     print(c.draw())
#     main()