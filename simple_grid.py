








import pygame


class Component_:

    def __init__(self, surface, color, pos, size):
        self.surface_ = surface
        self.color = color
        self._pos = pos
        self._size = size
        self.update()
        pass

    def update(self):
        self.surface = pygame.surface.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.pos
        self.surface.fill(pygame.color.Color(self.color))

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos
        self.update()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
        self.update()


class Grid_:

    def __init__(self, surface, columns, rows):

        self.surface_ = surface
        self._columns = columns
        self._rows = rows

        self._grid = []
        for row in range(rows):
            self._grid.append([])
            for column in range(columns):
                self._grid[row].append(0)
        pass

    def add_(self, component, column_span=1, row_span=1):
        for row_ind, row_obj in enumerate(self._grid):
            break_ = False
            for column_ind, column_obj in enumerate(row_obj):
                if column_obj == 0:
                    component.pos = [self.surface_.get_width() / self._columns * column_ind,
                                     self.surface_.get_height() / self._rows * row_ind]
                    component.size = [self.surface_.get_width() / self._columns * column_span,
                                      self.surface_.get_height() / self._rows * row_span]
                    true_false = []
                    for row_s in range(row_ind, row_ind + row_span):
                        for column_s in range(column_ind, column_ind + column_span):
                            if self._grid[row_s][column_s] != 0:
                                true_false.append(1)
                            else:
                                true_false.append(0)
                    if 1 in true_false:
                        break_ = True
                        raise "overlaying"
                        pass
                    else:
                        for row_s in range(row_ind, row_ind + row_span):
                            for column_s in range(column_ind, column_ind + column_span):
                                try:
                                    self._grid[row_s][column_s] = 1
                                except:
                                    raise "overlaying"
                    self._grid[row_ind][column_ind] = component
                    break_ = True
                    break
            if break_:
                break
        self.update()
        pass

    def attach_(self, component, column, row, column_span=1, row_span=1):
        column = column - 1
        row = row - 1
        if self._grid[row][column] == 0:
            component.pos = [self.surface_.get_width() / self._columns * column,
                             self.surface_.get_height() / self._rows * row]
            component.size = [self.surface_.get_width() / self._columns * column_span,
                              self.surface_.get_height() / self._rows * row_span]
            true_false = []
            for row_s in range(row, row + row_span):
                for column_s in range(column, column + column_span):
                    if self._grid[row_s][column_s] != 0:
                        true_false.append(1)
                    else:
                        true_false.append(0)
            if 1 in true_false:
                raise "overlaying"
            else:
                for row_s in range(row, row + row_span):
                    for column_s in range(column, column + column_span):
                        try:
                            self._grid[row_s][column_s] = 1
                        except Exception as error:
                            raise "overlaying"
                self._grid[row][column] = component
        else:
            raise "overlaying"
        self.update()
        print()
        for row in self._grid:
            print(row)
        pass

    def update(self):
        for row in self._grid:
            for column in row:
                if not isinstance(column, int):
                    self.surface_.blit(column.surface, column.rect)
        pass


class App_:

    def __init__(self):

        self.surface = pygame.display.set_mode([360, 360])
        self.quit = False
        self.clock = pygame.time.Clock()
        self.fps = 60
        pass

    def run(self):

        Component_1 = Component_(self.surface, "green", [100, 100], [20, 20])
        Component_2 = Component_(self.surface, "yellow", [100, 100], [20, 20])
        Component_3 = Component_(self.surface, "lightblue", [100, 100], [20, 20])
        Component_4 = Component_(self.surface, "orange", [100, 100], [20, 20])
        Component_5 = Component_(self.surface, "brown", [100, 100], [20, 20])

        Grid_1 = Grid_(self.surface, 3, 3)
        Grid_1.add_(Component_1, 2,2)
        Grid_1.attach_(Component_2, 3, 1, 1, 2)
        Grid_1.attach_(Component_3, 2, 3)
        Grid_1.add_(Component_4)
        Grid_1.add_(Component_5)

        while not self.quit:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.quit = True
                    pygame.quit()

            self.surface.fill(0)

            Grid_1.update()

            pygame.display.flip()
            self.clock.tick(self.fps)

        pass


if __name__ == "__main__":

    App = App_()
    App.run()