import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        point1 = data.Point(4,6)
        point2 = data.Point(6,8)
        result = hw2.create_rectangle(point1,point2)
        expected = data.Rectangle(data.Point(4,8),data.Point(6,6))
        self.assertEqual(expected,result)

    def test_create_rectangle_2(self):
        point1 = data.Point(6,8)
        point2 = data.Point(-2,-8)
        result = hw2.create_rectangle(point1,point2)
        expected = data.Rectangle(data.Point(-2,8),data.Point(6,-8))
        self.assertEqual(expected,result)

    # Part 2
    def test_shorter_duration_than_1(self):
        duration1 = data.Duration(4,50)
        duration2 = data.Duration(4,50)
        result = hw2.shorter_duration_than(duration1,duration2)
        expected = False
        self.assertEqual(result,expected)

    def test_shorter_duration_than_2(self):
        duration1 = data.Duration(4,50)
        duration2 = data.Duration(4,20)
        result = hw2.shorter_duration_than(duration1,duration2)
        expected = False
        self.assertEqual(result,expected)

    def test_shorter_duration_than_3(self):
        duration1 = data.Duration(4, 20)
        duration2 = data.Duration(4, 50)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = True
        self.assertEqual(result, expected)

    # Part 3
    def test_songs_shorter_than_1(self):
        song1 = data.Song("Marshmellow","Alone", data.Duration(2,30))
        song2 = data.Song("Jake Paul","Its Everyday Bro", data.Duration(1,59))
        song3 = data.Song("KSI","Thick of it", data.Duration(2,15))
        lista = [song1,song2,song3]
        result = hw2.songs_shorter_than(lista,data.Duration(2,20))
        expected = [song2,song3]
        self.assertEqual(expected,result)

    def test_songs_shorter_than_2(self):
        song1 = data.Song("Marshmellow","Alone", data.Duration(1,30))
        song2 = data.Song("Jake Paul","Its Everyday Bro", data.Duration(1,9))
        song3 = data.Song("KSI","Thick of it", data.Duration(2,15))
        lista = [song1,song2,song3]
        result = hw2.songs_shorter_than(lista,data.Duration(1,50))
        expected = [song1,song2]
        self.assertEqual(expected,result)

    # Part 4
    def test_running_time_1(self):
        song1 = data.Song("Marshmellow","Alone", data.Duration(1,30))
        song2 = data.Song("Jake Paul","Its Everyday Bro", data.Duration(1,10))
        song3 = data.Song("KSI","Thick of it", data.Duration(2,15))
        lista = [song1,song2,song3]
        listb = [0,0,2,1]
        result = hw2.running_time(lista,listb)
        expected = data.Duration(6,25)
        self.assertEqual(expected,result)

    def test_running_time_2(self):
        song1 = data.Song("Marshmellow","Alone", data.Duration(1,30))
        song2 = data.Song("Jake Paul","Its Everyday Bro", data.Duration(1,10))
        song3 = data.Song("KSI","Thick of it", data.Duration(2,15))
        lista = [song1,song2,song3]
        listb = [0,0,2,1,2,2,2,1]
        result = hw2.running_time(lista,listb)
        expected = data.Duration(14,20)
        self.assertEqual(expected,result)


    # Part 5
    def test_valid_route_1(self):
        lista = [["stockton","lathrop"],["stockton","tracy"],["tracy","acampo"],["acampo",'lodi']]
        listb = ["stockton","tracy","acampo","lodi"]
        result = hw2.valid_route(lista,listb)
        expected = True
        self.assertEqual(expected,result)

    def test_valid_route_1(self):
        lista = [["stockton","lathrop"],["stockton","tracy"],["tracy","acampo"],["acampo",'lodi']]
        listb = ["tracy","stockton","lathrop"]
        result = hw2.valid_route(lista,listb)
        expected = True
        self.assertEqual(expected,result)

    def test_valid_route_1(self):
        lista = [["stockton","lathrop"],["stockton","tracy"],["tracy","acampo"],["acampo",'lodi']]
        listb = ["lodi","tracy","acampo"]
        result = hw2.valid_route(lista,listb)
        expected = False
        self.assertEqual(expected,result)

    # Part 6
    def test_longest_repitition_1(self):
        lista = [2,2,2,3,3,3,4,4,4,4,5,5,5,5]
        result = hw2.longest_repetition(lista)
        expected = 6
        self.assertEqual(expected,result)

    def test_longest_repitition_2(self):
        lista = [1,2,2,3,3,3,5,5,5,5,5,4,4,4,4]
        result = hw2.longest_repetition(lista)
        expected = 6
        self.assertEqual(expected,result)




if __name__ == '__main__':
    unittest.main()
