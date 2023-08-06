from unittest import TestCase

from py_it_crypto.logs.access_log import AccessLog
from testutils import pub_A, priv_A, pub_B, priv_B, create_fetch_sender
from py_it_crypto.user.user import UserManagement

goDecryptB = '{"protected":"eyJhbGciOiJFQ0RILUVTK0EyNTZLVyIsImVuYyI6IkEyNTZHQ00iLCJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiIxaWZubjkwRFJxdEhHWEhyeHBhbC13NjZhemtBTERQU3hvNHF5RzRRdGhVIiwieSI6ImZVNGVEVUxmbFJldGQ2Z0MxZzJaTFYxMmFTeVl2dlZZVXgydzk4TjlRTGMifSwib3duZXIiOiJyZWNlaXZlciIsInJlY2lwaWVudHMiOlsicmVjZWl2ZXIiXX0","encrypted_key":"UVgAzNy22Zr47bfxPGLgYmxMtYAIvRt85DWURqiw4wZRzNt8Tup5Ew","iv":"cvz26Qr_Eri1eZ6i","ciphertext":"VylfB2FMOBH-fhceN9-Mv4jcvwRZXV1TapHF4gm9ZrlLVhD4GxQHQbT-KfrMn3SJtx7-Q6MmQIRtwIdJVnvuFHpdfW3VFOy2gPMhoEKhu1NpAZIChl9T4Hj9cZZjNGCvYSaZ8Th8X0JjbzjVVU5MolKm15mCUm_owsBA1MGrQYbK0Pe086YHcxWv1iSm4oEL8Y2mriwFmAIWP3Xu-q2eNnDvuzNrV4hM81pvWCuFAO6QQyO6IWsd5mQ4gt2QIiNu9zIgpOEKpGUlUYL02VQqwEv2GGK3vIyCF6cXo1kRnbNRHVQg6bIW3O6TuCgo4jadmz0Ja7oUNnW2wgWreiBE7uAD55xMbs9B5ModlnbunonLYryV1jS6jd6uB6svyRYnZ8Zd-4OoJl8lx5B6ry2-5HqH_Jtuo2iXwlsurszweBOSNg4gA3lPar4_Zzfljf4oiQS615eq347vXSQB0lkmToqATNZjlywaj7VLF5Lii1fDSMUpI1JI0VTPphOw4mT7a3XSVDs45B5y_pQ5ROn2kCPSjrkpLGRGewMPZQGzCMj_AjOl9pkQmEsvl0a-jJpmLkVGjK1Tm3MaYz3Cr1-XyfP74QId6QMDZzuE6i8lmlOlf6NEe_OuOfA5Abf388u7xLkq3y3hvEetS_FHVbd7qumnGgK7teORtPxM4LsB6CG7HUkWPcX6LbcZuK7kIfsrD2Rsz3jqp8RRlWWNU0uwcdjwZDCaLVl24lq307vHzFtGiNs0xnzfggcUOcG_i-eUsDAdSNTs0yP-jvzwmOmjIDc0_7w2NA6fRa7XyQK-obEM3Dw9BnnyD9jpoH9NtGDqDPbtttFRV7druW-KXg4SZQ557Ch4CA1LcyipXsS7tUAZF3pHFRdHrmHqYB39KiZOqjd6HVnk70VzoTWh5_ZRUEfqmK8W1CCPnQ","tag":"xh2lGFAM-8AK-39B-zaLzw"}'

goDecryptAB = '{"protected":"eyJlbmMiOiJBMjU2R0NNIiwib3duZXIiOiJyZWNlaXZlciIsInJlY2lwaWVudHMiOlsicmVjZWl2ZXIiLCJzZW5kZXIiXX0","recipients":[{"header":{"alg":"ECDH-ES+A256KW","epk":{"kty":"EC","crv":"P-256","x":"rAEKSPYdJdJ6bHPYrobWCBP1bxgA4uq7rF_xm-5O51U","y":"wLkRfalS1AmaYB29U7nkHzY4kKFhwA6rGO_GMinPwic"}},"encrypted_key":"YT1kMwqtXDg4MRxb9Qgpje1SbkQtCdxJwkfd1BCdKd5jlAlR5dA-Vg"},{"header":{"alg":"ECDH-ES+A256KW","epk":{"kty":"EC","crv":"P-256","x":"aWmlj9hKxT-3oRzsDgqgdk9slceHuoGCt37vdfWM97g","y":"B94CRu3_WGVy2hfVNQFRLyLbdYNTXloqRLoIQIBV-AA"}},"encrypted_key":"BTvPWcvVsmW80x18aW6UPUXIkRAwoKhFu9Ma8IQ7UCeFsQ2OU_50gw"}],"encrypted_key":"YT1kMwqtXDg4MRxb9Qgpje1SbkQtCdxJwkfd1BCdKd5jlAlR5dA-Vg","iv":"aYanSN64oJp-MRN5","ciphertext":"2iXDIW8b8GQ7Et2fO01RpnqV4ALfNBEipdhDrzSvNH98VQmm47RTuWtEclm_-OhtSBhqgHfshbmxlHwyTC4lHI-CGwmuMEuAR4G0586D8QllDenqGMgkaFl4a5oCInHkylxpWcWEr_Sv0uf0br4UpU3sLRLkyZQ5INKflRYkiu-umeN__xxNyKC4e8CD2waqk6u8IlBWX5dUTmEEDWtfDugNaPLZ0xzVWzTwLY5I_P23CFAjTAbBNFwJS6IyJU2HQz-i-pPMgRv2qJ2V6ikJ6KRy0FD_N9kSiHc3gwM3Wu6_PvV3b4nLW7lPeUG6BAOjfwXzvo1T-RwxD8ocqXKk8ctk8H5iKffGlSnugtnY5nBUl69hTPUzhfKL9dOG6QxAhMbkwZh79pofJJ6jx0eFxssDQ-eWFwIfAfMFeDGA9watJAs5VbMKF2jGm6huyxq8cMI3z5N5is9J7qB3R844vLTvHzx-2Qdcrd7x0t_Grk21_nXyCJr8oja4dH6kPVz5PgDPHvVqV4xpAwSQqFoSKlo3T65zkV3AQPGyPO3HFD129ZbNW34OS0plFGUONrL4zfiOqq8YZ7Vgt-1eo0BFnrD9yfjMNwwFr_41-h4_KXI7bAVtzq1kFelx_xmAc9tIEf8rr6yDRhfK6qOzQ-En2LgNl4J1G8WgtglYUUtbDh9dcN6vOwBxC2LB6YNUDebjsJ6c_NK1xcGcPQhObTa3XfIq4qrYZcbdJuNGsENV27NgMd5HrnvJo-G1xsVKCVlnryUeO5MZtmYTKwjjA1-K1wYU4v6cBHaab-aTUPElK7pNfSjPUYTLJVXcyFTzrcvceAkJl-gBlYksH-N0hFMYsQNd55fpbvERjxaSNPu_R4f9VMO_J6TVKKsu7Rn0S2D-W2fPN0KFhBemdyrFtdHrjl4x2LRIPVJa-Tsskc3CThZ6T1bJRCyf-A","tag":"HKUO2q1hTVGnS53s7g7Kcw"}'

pythonDecryptB = '{"ciphertext":"c6Vbldc2ZdrnBd4CURrvVd1g_ahctN-vZHf76ct8OKCXNPFYMm_AMajxzKYLs5gA5glXnEUNm54zShF1qD_P91T8Jc8fbu0cTy80uWGoHhcEfNMa_92P1BQL6H95vp4Cdy06pr1RAw5I-7ZJhfVNR1f-Pt-JV0OK4Jd-5Ei_tY0RkWkPoebhgzgkmGqToJMnp6c6NQMUUt-DpHusc6rqwpkw56t4TnEsRgHthoST_Mp0x6ovsxjgLq33wri1_WNtdw4R-aFXeEiO6nzWKqpf8Gpnh4RTc1dMI_DIbjNWWNkMebH8ICiJIqA4XSopiwekbud9TBKVwxPUKv0wk3l6vUMZxcv2_nKIne3u7fIL7rIMpgrTREio8o0ptIW7L_ezF93BWnto7B7AT_T2x-cEVrfhcaBf-1aN8XGIzX4kr-VUwX-UL0AC_jtYlVuz5tR_wVNWGhWQBMhSO9pEsgtEyVBFTcD2wg6jmRF4YqXZ6GBdaaDXyV8GOwb62Sk509IeMDL40_D8mdgCPLZmzDsYoFWXRGNsFXi7bb3NoHSXwsGG4itvZRJ1x3ov9TfK7p2bVnn974SrtuBZZKKG-xzF8ItDsc22xRsacSayX4Z6Iat9Y7oA3XFuAubwCwlmLEX76995BK77Pw8zWW76_-R8tG67vfQ8aq-RhNR12EndeJtmlkiKBVl6YJvr85dDzeRvO-ZZsbvL83CrL4VH3-66P5L1juZCNekNGuAYK7FYy_YDIiQSSk2OHzsXjuFnzy5mqUny-qlLSHB05DGm4PFC_A82Mzu_fiQxV3advPWturzsIQbNZHA5gaFw8RngwIfIKaD9m1SZuNWmiwn5hOc2tZi6-S6QZLG5omwgEQkIeERxU6y2r0H68Cc79OVxnUhVG5DZvVKJotXrQDxp7nU6S5n3T1idYgA-","encrypted_key":"RcK0ND_f4O434Ev4G-BTnQaow8fO2ywebat7E3dd8bnSDhXntZUNuw","header":{"epk":{"crv":"P-256","kty":"EC","x":"1tgSv36dPChq7QpQHVJgNmXt_Ijgu8R6VUGH_Q-FhnY","y":"2NpgsNKcMWXnd4q63dSFIKbwQkrayW9oDmDDkZGXdxE"}},"iv":"Xfu555nNhPaKWFd8","protected":"eyJhbGciOiJFQ0RILUVTK0EyNTZLVyIsImVuYyI6IkEyNTZHQ00iLCJvd25lciI6InJlY2VpdmVyIiwicmVjaXBpZW50cyI6WyJyZWNlaXZlciJdfQ","tag":"6AV5Q7g8XN9aHnIlGqKBTQ"}'

pythonDecryptAB = '{"ciphertext":"caNbail0LsXJiEAyz6yD1HORJrapqe1-AB80OhtfH6JURAYItlPLOuokmq8pYlSuoL2SkI-61OHMLMaLgHMEnres39KlfADysd_BijdB7QxTKDTz_6Cgp2bESiIHYvq9Ub7qmZOK13rk5uFPRR-vJlXpt-idAtJUmDPCktwzDhnH8nhPDaMoxtc_YV4jll8esv79VIRiEW4XoLKxpTnY4vwgUAqck_VkOWvKFhKLAVJG2eLQa5i4mS1UOCJ5gpjVo2R26LkffJTBlM3J9MQdHKcGeKKuS7xcEPgCVQA-XymN1NReAd90fnCwnTOt9fR0dHMGy9IqbEwCu4z2JQIOSal5Q9CWVozNjUVVohYPYG1BqVdHhVkL3VGNC1tfXNS-fEUDg4q8NACppBBQlbHD_EaF5h0zpX0aa_GfNwG2GjC06pV0Wh8OcEhd7rBjhd6xoqEwCKsjFYLZGFwxX1VGdjHS4GbhYNTZjzSXZLKM-2vZUBTvpZ-6Z2G04j3m8j09h3FROnqJWe_STK-fik3lXE9bcA-0J4E2IIFhljAaPYhQ0EPbF1xpOqyKPoMx8XKkRr-MzXKD4RP2k_J69caPcXnFdqPmtdxvLwgKeenf-MR-a3XrqotLGTyXdcRk9XR8g3eAP0AI-JvIIQm_U_NCab8MVRNVnJjQWbLVzy4atTWlfLhd-vH-uQ9DWy51WrkTnLY9bDzHF0Mx2A0riANbgSxejgTtmVipYRAJhjNGVNFs2jDlph66NU9gy6K7z1crRi1D87d_jQqrvobiXmMf5dD7DUkPPGIvKNFEbWq9JLNbbP13AvR9k2-rwWJpjPuOMqQb08RjhJDMAZ_LDUu1Hj3B--Da6qFFSLino7yZS5V1WkWgsjq4OjvM31HbpbWkYkGnwwkaykMsqlz_erdb-ViCQNbP8yaA7lCx1M1opZvSUEVvq8Y","iv":"zCwToOHugJJAnZny","protected":"eyJhbGciOiJFQ0RILUVTK0EyNTZLVyIsImVuYyI6IkEyNTZHQ00iLCJvd25lciI6InJlY2VpdmVyIiwicmVjaXBpZW50cyI6WyJyZWNlaXZlciIsInNlbmRlciJdfQ","recipients":[{"encrypted_key":"aIisPIB9gm4GOVgiDTctP4r8zj2TMNgt9WcNWNZ0BdOUMohqyFmPHg","header":{"epk":{"crv":"P-256","kty":"EC","x":"oIy4oVXzDnNTWDeZS-Q8JzDhWmrEkUDzxCJq_F3BluI","y":"qJlzqJrbaSVWkiTWKTa0StJrlfq3KacAo-SlXgCkWqI"}}},{"encrypted_key":"Evhnk_zTOITfl3KVAkV2HDBRuZ39cIOcvkBdTtzTtu-B1rXVh2otVQ","header":{"epk":{"crv":"P-256","kty":"EC","x":"siMarkEyyKHGzpYAJZ6UUzBBb0eTHJktZmxis5-OAQ8","y":"Nw45SYXhkdTqLntZjLkbnLchTD46myk4kWPRcIYB_vM"}}}],"tag":"TxKoh7C01WmG0QFQpFBTWA"}'

jsDecryptB = '{"ciphertext":"bZlgs-8XeAzjHiWbcydItX88Vw8vKDH8z7aSUL1oQRPkTiE12WnehTmpTLIGMtKSKvMvSnF4-NZJ4WErMzRM7u8tMcPkbTHuOsK5ElR-4Y4JlgMt-tpI1CtekL6pHZj4K4rfBQH7kxUHtcbuOxSxPjHgQ4vR7lBNRcFxBdJJ4oCyn4JlCkY5DjZjr57KYCfuhnluau5ThZbvh5LvMYzg9btmJc_xTiLkD2GoxYwdULqt6EGRGkr6wUnkNM_MmK-7OaXOSLPRbGtFpslui7wyxXQhUijSPUhltaBbSzQx9-Ofb5GHNz93gSSVQSu3bFebINDfMrPTMcp7yruq-a08t0NWiHoF-TqHxexhOzZ_RPdzHLnmK_W0LEJxhZvHwcldIdPIc25Pab2QRxr7ypO6IktDVRLj4ac2oJ4AatvwCqAV70Jc_NL5AGurjSLNUMV0GHw7QAqy4eyQBO2HPxnl5n7mGupPAsWfhoxOpRauxU1-PQDqOKZmKfafSm907_nTnHHaeQPrY8OwbJGZl3EHzZJEHE2hBVmQVmZgdK8FLF4nuPxWD2Z2mEOzGcWUtBvuo7gYgUoueNdOI5CAOJMKJXrSihwJMETcHwuTt6PrfTvWinsy3y5S-uQkkxGN5EkCXuzrSGp9Oak2bpurz5ezUKnL1IYmo9m7wC52O7kW0IGJ6B-URr8XHisXXrTrX9SoEOb11Tz5XnGPJP27KJKp1ydrgQLsvUzWz9o1QdJK-lEqigj0CIgmx_UTVuNBRZuz5UAe2mJQ0yhpLGJVyzGJjTwW_5_ZZxXv9S5Qr8oVi7h-dMENqdCuxJPD9dBMR5iFE3kFior98hNRs5C0CokOfmpfLpJXqBjs2a9H5PXSU5UGeUj6_jPjmFldcRga63T4vkV8N3e-Pg5UKEIYzQBQJ22WPbVKlCBuzjh3dmfM","iv":"9hIFX0Nc-WOnz124","recipients":[{"encrypted_key":"747LVKTbu6zRNSgQhAzIVIjwvE-fiUzk5Jvbe6Qg84Hzc87_UlUQaw","header":{"alg":"ECDH-ES+A256KW"}}],"tag":"hmb-Aezjbwuqc8nusvJCgQ","protected":"eyJlbmMiOiJBMjU2R0NNIiwicmVjaXBpZW50cyI6WyJyZWNlaXZlciJdLCJvd25lciI6InJlY2VpdmVyIiwiZXBrIjp7IngiOiJRT2Jpd09OVTZTeTRleUVsWlJXSEtmd2t4U2liSS1rejBLUjhTdVc3N3g0IiwiY3J2IjoiUC0yNTYiLCJrdHkiOiJFQyIsInkiOiIxZmdXM1k5QnFVb1Q5NU9nVkpCM0ktWUFHd1czaDM3N1ZNV0NneVNBaTNBIn19"}'

jsDecryptAB = '{"ciphertext":"5N8_RLJ-LqeHveNGvgixFi0YNsIwspTaFGRIUOkIqI8fKri1mS3fcXYgDZBvo4KfuueuILFMXsnRzzfWtfkK28wUekzpw33p4OvRneuKI_5xN6k95PP8-iZ8Dj3fwaKooiiWnHAZXZ_9Pyd_Vp1svJli_5MtQL6dAyIFWEGMI23TOHIlv4Y_WIoqzTMr8p8Ngsa1valCipNJXdpi_IcPrj8c8vNCRdxkjli5BiotBAxOPb1dkm4rygRTXe5r48yaQ41I8Sn0lYcUL1f833wHT5dBZcy6dnkVbxXzKjpCRzqzxK3WLbu1buF1MiNVzQfVWi3NPRCF2MkJvW8z6qULTc_cREOQmoRCdORN8X0xv0ySCy7x-b2kqlJXp1cX7oCpPtst8JrEHu6KN2R3glgHXaqazH4EJr3uTXgtqTmL4oaxDoFc0dpHfA4X4tvF3MBdWzib8ExAeUkRGEjaWf98fx6Mnc8NiePRUfdISyaoiUU_Kx5yOkRdKznJugLdc9T3IrAyQlKa0Z4XDuRkjdlDL0B7vf5ijZRccp8iG7ugwBZbYSdSElmzUwjI9r08eSXUYDK2u6RV3yYENwhky-ZRn42ugHrX0DYjNOB1eflrp_JQ-DANExG5cnb9uouKXoIUjbvoRGJVtXde9oKKGMN7XkiNBmn2vgmfuu9z-u59tUCEgMP8rKmUEBWR4AL3pW8V4K6XLpNRFB0flXZy4xbh5VWWfZfQvSOXEkjpDQedBoACPXroY1zkfI2eGegxwwl-gplQk1nHSSd24bMh07yWZWQBOJJBJN1DUQUjfaW75rvmZnDupadS-Hbzbdvd7mu4FopRECuQh3twHvYh7wa6K6UcQG9a6gM71jo8vDASNY48nDJVDU9rCwiyNYdea1LFfBkfvgadsREaIs_WzN7ndz3VCoRNrCCZNtL48ZkAnTWaVhkXb0BjM8LIuWmh","iv":"UhExTANI5WfvWz9Q","recipients":[{"encrypted_key":"bSzBVL-v5gDy_kldRKC4CsdyoTudd-a1jkUOGGd0DWRURI0LKmFuCg","header":{"alg":"ECDH-ES+A256KW","epk":{"x":"lwaGgrNt7j6G7ZYUs62xSxK9GypRdSUWTMGCzeUEHoI","crv":"P-256","kty":"EC","y":"JkYhU-avgsLxNWy2qddcwggph4ImCqNTvXutCHq81cg"}}},{"encrypted_key":"oXLukazxtuxXN5FfvIOtVsH21ul-4RzhEfyPHNchNI5qHKSHjK7-HA","header":{"alg":"ECDH-ES+A256KW","epk":{"x":"dsHx4hcFu7yLJLTJLmTvebnk7nua_oWKAu6LXewVWpo","crv":"P-256","kty":"EC","y":"r3G8A8XCR3bhK5kdoOvqvlCOiGtGQqQlU0gF50St_5M"}}}],"tag":"tO_69F0pamJCuC6EeMq_cg","protected":"eyJlbmMiOiJBMjU2R0NNIiwicmVjaXBpZW50cyI6WyJzZW5kZXIiLCJyZWNlaXZlciJdLCJvd25lciI6InJlY2VpdmVyIn0"}'

sender = UserManagement.importAuthenticatedUser('sender', pub_A, pub_A, priv_A, priv_A)
sender.is_monitor = True
receiver = UserManagement.importAuthenticatedUser('receiver', pub_B, pub_B, priv_B, priv_B)


class TestCompatibilityGo(TestCase):
    """Test compatibility with go-it-crypto lib"""

    def test_single_receiver(self):
        """Test if receiver can decrypt goDecryptB"""
        log = receiver.decrypt_log(goDecryptB, create_fetch_sender([sender]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "go-it-crypto")

    def test_multiple_receiver(self):
        """Test if receiver and sender can decrypt goDecryptB"""
        log = receiver.decrypt_log(goDecryptAB, create_fetch_sender([sender, receiver]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "go-it-crypto")

        log = sender.decrypt_log(goDecryptAB, create_fetch_sender([sender, receiver]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "go-it-crypto")


class TestCompatibilityJS(TestCase):
    """Test compatibility with js-it-crypto lib"""

    def test_single_receiver(self):
        """Test if receiver can decrypt jsDecryptB"""
        log = receiver.decrypt_log(jsDecryptB, create_fetch_sender([sender]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "js-it-crypto")

    def test_multiple_receiver(self):
        """Test if receiver and sender can decrypt jsDecryptB"""
        log = receiver.decrypt_log(jsDecryptAB, create_fetch_sender([sender, receiver]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "js-it-crypto")

        log = sender.decrypt_log(jsDecryptAB, create_fetch_sender([sender, receiver]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "js-it-crypto")


class TestCompatibilityPython(TestCase):
    """Test compatibility with py-it-crypto lib"""

    def test_single_receiver(self):
        """Test if receiver can decrypt pyDecryptB"""
        log = receiver.decrypt_log(pythonDecryptB, create_fetch_sender([sender]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "py-it-crypto")

    def test_multiple_receiver(self):
        """Test if receiver and sender can decrypt pyDecryptB"""
        log = receiver.decrypt_log(pythonDecryptAB, create_fetch_sender([sender, receiver]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "py-it-crypto")

        log = sender.decrypt_log(pythonDecryptAB, create_fetch_sender([sender, receiver]))
        accessLog = log.extract()
        self.assertEqual(accessLog.justification, "py-it-crypto")


class TestCreateCompatibilityTokens(TestCase):

    def test_create_tokens(self):
        """Create tokens for compatibility tests"""
        access_log = AccessLog.generate()
        access_log.owner = receiver.id
        access_log.monitor = sender.id
        access_log.justification = "py-it-crypto"

        signed_log = sender.sign_log(access_log)
        pythonDecryptB = sender.encrypt_log(signed_log, [receiver])
        pythonDecryptAB = receiver.encrypt_log(signed_log, [receiver, sender])
        print(pythonDecryptB)
        print(pythonDecryptAB)