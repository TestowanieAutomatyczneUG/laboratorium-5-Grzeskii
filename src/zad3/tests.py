import unittest
from song import Song

class SongLinesTest(unittest.TestCase):
    
    @unittest.skip("skipping")
    def test_print_first_line(self):
        self.assertEqual(Song.line(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")
    @unittest.skip("skipping")
    def test_print_third_line(self):
        self.assertEqual(Song.line(3), "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")
    @unittest.skip("skipping")
    def test_print_lines_between_two_and_five(self):
        self.assertEqual(Song.fewLines(2,5), ["On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."])
    @unittest.skip("skipping")
    def test_print_lines_between_same_number(self):
        self.assertEqual(Song.fewLines(5,5), [])
    @unittest.skip("skipping")
    def test_print_whole_song(self):
        self.assertEqual(Song.wholeSong(), ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.", "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.", "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.", "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."])
    @unittest.skip("skipping")
    def test_disallow_numbers_bigger_than_number_of_lines(self):
        with self.assertRaisesWithMessage(ValueError):
            Song.line(15)
    @unittest.skip("skipping")
    def test_disallow_negative_numbers_of_lines(self):
        with self.assertRaisesWithMessage(ValueError):
            Song.line(-8)
    @unittest.skip("skipping")
    def test_disallow_second_number_smaller_than_first(self):
        with self.assertRaisesWithMessage(ValueError):
            Song.fewLines(5, 2)
    @unittest.skip("skipping")
    def test_disallow_negative_numbers_of_fewLines(self):
        with self.assertRaisesWithMessage(ValueError):
            Song.fewLines(-4, -9)
    @unittest.skip("skipping")
    def test_disallow_type_other_than_int_in_line_method(self):
        with self.assertRaisesWithMessage(TypeError):
            Song.line("trzecia")
    @unittest.skip("skipping")
    def test_disallow_type_other_than_int_in_fewLines_method(self):
        with self.assertRaisesWithMessage(TypeError):
            Song.fewLines(3, True)
    
    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp
    
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

if __name__ == '__main__':
    unittest.main()
    