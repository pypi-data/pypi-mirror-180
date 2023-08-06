from .protocol.gen_tp_docx import GenTpDocx
from .protocol.gen_tp_pdf import GenTpPdf
from .protocol.gen_tp_txt import GenTpTxt
from .summary.gen_summary_docx import GenSummaryDocx
from .summary.gen_summary_pdf import GenSummaryPdf
from .summary.gen_summary_txt import GenSummaryTxt
from .trace_matrix.gen_trace_matrix_pdf import GenTraceMatrixPdf
from .trace_matrix.gen_trace_matrix_txt import GenTraceMatrixTxt
from .. import services


# -------------------
## Generates all reports
# currently generates 3 types of reports:
#   * Protocol with results
#   * Trace matrix report
#   * Summary report
class Report:
    # -------------------
    ## constructor
    def __init__(self):
        pass

    # -------------------
    ## run all reports
    #
    # @return None
    def report(self):
        self._report_protocols()
        self._report_trace_matrix()
        self._report_summary()

    # -------------------
    ## run all protocol and reports
    #
    # @return None
    def _report_protocols(self):
        protocols = services.storage.get_protocols()

        # reports with results: txt, pdf and docx
        services.cfg.page_info.set_tp_protocol_cfg()
        gtt = GenTpTxt(protocols, do_results=False)
        gtt.gen()

        gtp = GenTpPdf(protocols, do_results=False)
        gtp.gen()

        # TODO temp.
        gtd = GenTpDocx(protocols, do_results=False)
        gtd.gen()

        # test protocol (no results): txt and pdf
        services.cfg.page_info.set_tp_report_cfg()
        gtt = GenTpTxt(protocols, do_results=True)
        gtt.gen()

        gtp = GenTpPdf(protocols, do_results=True)
        gtp.gen()

    # -------------------
    ## run all trace matrix reports
    #
    # @return None
    def _report_trace_matrix(self):
        services.cfg.page_info.set_trace_cfg()
        matrix = services.storage.get_trace()

        gtt = GenTraceMatrixTxt(matrix)
        gtt.gen()

        gtm = GenTraceMatrixPdf(matrix)
        gtm.gen()

    # -------------------
    ## run all summary reports
    #
    # @return None
    def _report_summary(self):
        services.cfg.page_info.set_summary_cfg()
        summary = services.storage.get_summary()

        gst = GenSummaryTxt(summary)
        gst.gen()

        gsp = GenSummaryPdf(summary)
        gsp.gen()

        gsd = GenSummaryDocx(summary)
        gsd.gen()
