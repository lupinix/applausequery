#
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#

# internal imports
from .. import tap_session

# Standard library imports

# Third party modules

__all__ = ['query_basic_lc_by_ucac4_id']

def query_basic_lc_by_ucac4_id(ucac4_id):
    query = "SELECT jd_mid,bmag,bmagerr,vmag,vmagerr \
        FROM applause_dr3.lightcurve \
        WHERE bmag IS NOT NULL \
        AND bmagerr IS NOT NULL \
        AND vmag IS NOT NULL \
        AND vmagerr IS NOT NULL \
        AND ucac4_id=\'%s\' \
        ORDER BY jd_mid" %(ucac4_id)
    lc = tap_session.run_async(query)
    return lc.to_table()
