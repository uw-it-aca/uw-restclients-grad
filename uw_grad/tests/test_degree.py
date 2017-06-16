import datetime
from unittest import TestCase
from restclients_core.exceptions import DataFailureException
from uw_grad.degree import get_degree_by_regid
from uw_pws.util import fdao_pws_override
from uw_grad.util import fdao_grad_override


@fdao_grad_override
@fdao_pws_override
class DegreeTest(TestCase):

    def test_get_request_by_regid(self):
        requests = get_degree_by_regid(
            "9136CCB8F66711D5BE060004AC494FFE")

        self.assertEqual(len(requests), 6)
        degree = requests[0]
        self.assertIsNotNone(degree.json_data())
        self.assertEqual(degree.req_type, "Masters Request")
        self.assertEqual(degree.submit_date,
                         datetime.datetime(2015, 3, 11, 20, 53, 32, 733000))
        self.assertEqual(
            degree.degree_title,
            "MASTER OF LANDSCAPE ARCHITECTURE/MASTER OF ARCHITECTURE")
        self.assertEqual(degree.major_full_name,
                         "Landscape Arch/Architecture (Concurrent)")
        self.assertEqual(degree.status,
                         "Awaiting Dept Action (Final Exam)")
        self.assertTrue(degree.is_status_await())
        self.assertFalse(degree.is_status_graduated())
        self.assertFalse(degree.is_status_candidacy())
        self.assertFalse(degree.is_status_recommended())
        self.assertIsNone(degree.exam_place)
        self.assertIsNone(degree.exam_date)
        self.assertEqual(degree.target_award_year, 2015)
        self.assertEqual(degree.target_award_quarter, "winter")
        degree = requests[5]
        self.assertEqual(degree.status,
                         "Did Not Graduate")
        self.assertTrue(degree.is_status_not_graduate())

    def test_error(self):
        self.assertRaises(DataFailureException,
                          get_degree_by_regid,
                          "00000000000000000000000000000001")
