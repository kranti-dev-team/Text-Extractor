import boto3
from trp import Document

# S3 Bucket Data
s3BucketName = "narenineuron"
PlaindocumentName = "Example_01.png"
# FormdocumentName = "Test3.JPG"
# TabledocumentName = "Test4.JPG"

ACCESS_KEY_ID = "AKIAQULFVLB7RMDVAR4Y"
ACCESS_SECRET_KEY = "sXGAvWCFidG7WkKpyXChLp942NKQe/sd/AUCDQ8t"

s3 = boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
)

# Amazon Textract client
textract = boto3.client(
    "textract",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    region_name="ap-south-1",
)

# 1. PLAINTEXT detection from documents:
response = textract.detect_document_text(
    Document={"S3Object": {"Bucket": s3BucketName, "Name": PlaindocumentName}}
)
print("------------- Print Plaintext detected text ------------------------------")
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        # print("\033[92m" + item["Text"] + "\033[92m")
        print(item["Text"])
        # if "Question" in item["Text"]:
        #     question = item["Text"]
        # else:
        #     answer = item["Text"]


# # 2. FORM detection from documents:
# response = textractmodule.analyze_document(
#     Document={"S3Object": {"Bucket": s3BucketName, "Name": FormdocumentName}},
#     FeatureTypes=["FORMS"],
# )
# doc = Document(response)
# print("------------- Print Form detected text ------------------------------")
# for page in doc.pages:
#     for field in page.form.fields:
#         print("Key: {}, Value: {}".format(field.key, field.value))


# # 2. TABLE data detection from documents:
# response = textractmodule.analyze_document(
#     Document={"S3Object": {"Bucket": s3BucketName, "Name": TabledocumentName}},
#     FeatureTypes=["TABLES"],
# )
# doc = Document(response)
# print("------------- Print Table detected text ------------------------------")
# for page in doc.pages:
#     for table in page.tables:
#         for r, row in enumerate(table.rows):
#             itemName = ""
#             for c, cell in enumerate(row.cells):
#                 print("Table[{}][{}] = {}".format(r, c, cell.text))
