from backend.converter.api.converter import *
import unittest
from unittest.mock import MagicMock, patch

class TestFileConversions(unittest.TestCase):
    @patch('backend.converter.api.converter.Document')
    def test_convert_docx_to_doc(self, MockDocument):
        mock_document = MagicMock()
        MockDocument.return_value = mock_document

        test_files = ['test1.docx', 'test2.docx']

        convert_docx_to_doc(test_files)

        calls_load = [((file,),) for file in test_files]
        calls_save = [((file.replace('.docx', '.doc'), FileFormat.Doc),) for file in test_files]
        mock_document.LoadFromFile.assert_has_calls(calls_load, any_order=True)
        mock_document.SaveToFile.assert_has_calls(calls_save, any_order=True)

    @patch('backend.converter.api.converter.Document')
    def test_convert_doc_to_docx(self, MockDocument):
        mock_document = MagicMock()
        MockDocument.return_value = mock_document

        test_files = ['test1.doc', 'test2.doc']

        convert_doc_to_docx(test_files)

        calls_load = [((file,),) for file in test_files]
        calls_save = [((file.replace('.doc', '.docx'), FileFormat.Docx),) for file in test_files]
        mock_document.LoadFromFile.assert_has_calls(calls_load, any_order=True)
        mock_document.SaveToFile.assert_has_calls(calls_save, any_order=True)