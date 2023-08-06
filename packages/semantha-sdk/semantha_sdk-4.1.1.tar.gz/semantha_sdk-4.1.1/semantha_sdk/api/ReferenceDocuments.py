from io import IOBase
from typing import Optional

from semantha_sdk.api import SemanthaAPIEndpoint
from semantha_sdk.model.Document import Document
from semantha_sdk.model.Entity import Entity
from semantha_sdk.model.NamedEntities import NamedEntities
from semantha_sdk.model.Paragraphs import Paragraph
from semantha_sdk.model.ReferenceDocuments import ReferenceDocuments as _ReferenceDocumentsDTO, \
    ReferenceDocumentCollection, Statistic
from semantha_sdk.model.Sentences import Sentence
from semantha_sdk.response import SemanthaPlatformResponse


class ReferenceDocuments(SemanthaAPIEndpoint):
    @property
    def _endpoint(self):
        return self._parent_endpoint + "/referencedocuments"

    def get_all(self) -> _ReferenceDocumentsDTO:
        """ Get all reference documents """
        return self._session.get(self._endpoint).execute().to(_ReferenceDocumentsDTO)

    def delete_all(self):
        """ Delete all reference documents """
        self._session.delete(self._endpoint).execute()

    def post(
        self,
        name: str = None,
        tags: str = None,
        metadata: str = None,
        file: IOBase = None,
        text: str = None,
        document_type: str = None,
        color: str = None,
        comment: str = None,
        detect_language: bool = False
    ) -> ReferenceDocumentCollection:
        """ Upload a reference document

        Args:
            name (str): The document name in your library (in contrast to the file name being used during upload).
            tags (str): List of tags to filter the reference library.
                You can combine the tags using a comma (OR) and using a plus sign (AND).
            metadata (str): Filter by metadata
            file (str): Input document (left document).
            text (str): Plain text input (left document). If set, the parameter file will be ignored.
            document_type (str): Specifies the document type that is to be used when reading the uploaded PDF document. 
            color (str): Use this parameter to specify the color for your reference document.
                Possible values are RED, MAGENTA, AQUA, ORANGE, GREY, or LAVENDER.
            comment (str): Use this parameter to add a comment to your reference document.
            detect_language (bool): Auto-detect the language of the document (only available if configured for the domain).
        """
        return self._session.post(
            self._endpoint,
            body={
                "name": name,
                "tags": tags,
                "metadata": metadata,
                "file": file,
                "text": text,
                "documenttype": document_type,
                "color": color,
                "comment": comment
            },
            q_params={
                "detectlanguage": str(detect_language)
            }
        ).execute().to(ReferenceDocumentCollection)

    def get_one(self, document_id: str) -> Document:
        """ Get a reference document by id """
        return self._session.get(f"{self._endpoint}/{document_id}").execute().to(Document)

    def delete_one(self, document_id: str):
        """ Delete a reference document by id """
        self._session.delete(f"{self._endpoint}/{document_id}").execute()

    def post_update(
            self,
            document_id: str,
            id: str,
            name: str,
            tags: list[str],
            metadata: str,
            file_name: str,
            created: int,
            updated: int,
            processed: bool,
            lang: str,
            content: str,
            documentClass: Entity,
            derived_tags: list[str],
            color: str,
            derived_color: str,
            comment: str,
            derived_comment: str,
            query_by_name: bool = False
    ) -> SemanthaPlatformResponse:
        """ Update reference document by id (not yet implemented)"""
        # TODO implement and adapt DocString
        raise NotImplementedError("Reference documents can not be updated yet")
        return self._session.patch(f"{self._endpoint}/{document_id}").execute()

    def get_paragraph(self, document_id: str, paragraph_id: str) -> Paragraph:
        """ Get a paragraph of a reference document by document id and paragraph id"""
        return self._session.get(f"{self._endpoint}/{document_id}/paragraphs/{paragraph_id}").execute().to(Paragraph)

    def delete_paragraph(self, document_id: str, paragraph_id: str):
        """ Delete a paragraph of a reference document by document id and paragraph id"""
        self._session.delete(f"{self._endpoint}/{document_id}/paragraphs/{paragraph_id}").execute()

    def patch_paragraph(self, document_id: str, paragraph_id: str) -> SemanthaPlatformResponse:
        """(not yet implemented)"""
        # TODO implement and adapt DocString
        return self._session.patch(f"{self._endpoint}/{document_id}/paragraphs/{paragraph_id}").execute()

    def get_sentence(self, document_id: str, sentence_id: str) -> Sentence:
        """ Get a sentence of a reference document by document id and sentence id"""
        return self._session.get(f"{self._endpoint}/{document_id}/sentences/{sentence_id}").execute().to(Sentence)

    def get_clusters(self) -> SemanthaPlatformResponse:
        """(not yet implemented)"""
        # TODO implement and adapt DocString
        raise NotImplementedError("Clustering of reference documents can not be activated via the SDK yet")
        return self._session.get(f"{self._endpoint}/clusters").execute()

    def get_named_entities(self) -> Optional[NamedEntities]:
        """ Get all named entities (aka custom entities) that were extracted from the reference documents.
        Note: Might be None iff no named entities have been extracted.
        """
        return self._session.get(f"{self._endpoint}/namedentities").execute().to(NamedEntities)

    def get_statistic(self) -> Statistic:
        """ Get statistics for reference documents"""
        return self._session.get(f"{self._endpoint}/statistic").execute().to(Statistic)
