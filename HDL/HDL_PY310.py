#   --------------------------------声明区--------------------------------
#   项目内所涉及任何脚本、LOGO、工作流仅为资源共享、学习参考之目的，不保证其合法性、正当性、准确性；请根据情况自行判断，切勿使用项目做任何商业用途或牟利；
#   本人不对任何内容承担任何责任，包括但不限于任何内容错误导致的任何损失、损害；
#   其它人通过任何方式登陆本网站或直接、间接使用项目相关资源，均应仔细阅读本声明，一旦使用、转载项目任何相关教程或资源，即被视为您已接受此免责声明。
#   本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。
#   本项目涉及的数据由使用的个人或组织自行填写，本项目不对数据内容负责，包括但不限于数据的真实性、准确性、合法性。使用本项目所造成的一切后果，与本项目的所有贡献者无关，由使用的个人或组织完全承担。
#   本项目中涉及的第三方硬件、软件等，与本项目没有任何直接或间接的关系。本项目仅对部署和使用过程进行客观描述，不代表支持使用任何第三方硬件、软件。使用任何第三方硬件、软件，所造成的一切后果由使用的个人或组织承担，与本项目无关。
#   本项目中所有内容只供学习和研究使用，不得将本项目中任何内容用于违法行为，包括但不限于建立 VPS 或违反国家/地区/组织等的法律法规或相关规定的其他用途。作者对于由此引起的任何隐私泄漏或其他后果概不负责。
#   所有基于本项目源代码进行的任何修改，为其他个人或组织的自发行为，与本项目没有任何直接或间接的关系，所造成的一切后果亦与本项目无关。
#   所有直接或间接使用本项目的个人和组织，应24小时内完成学习和研究，并及时删除本项目中的所有内容。如对本项目的功能有需求，应自行开发相关功能。
#   本项目保留随时对免责声明进行补充或更改的权利，直接或间接使用本项目内容的个人或组织，视为接受本项目的特别声明。
#   严禁将本项目用于恶意软件投递、规避安全检测、未授权渗透、免杀处理、流量隐藏或任何违反网络安全法律法规的行为。
#   --------------------------------祈求区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
#
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
"""
 ██████  ███████
██    ██ ██
██    ██ █████
██ ▄▄ ██ ██
 ██████  ██
Create at [2026-07-10 23:24:47 ]
Protect by 清风
"""
#   --------------------------------使用说明区--------------------------------
#   '''
#   vx小程序 -- 海底捞
#   export HDL_TOKENS="openId1#unionId1@openId2#unionId2" 多账号使用 "@" 分隔
#   '''
#   ------------------------------------------------------------------------
import base64
import hashlib
import hmac
import importlib.machinery
import importlib.util
import json
import os
import platform
import sys
import tempfile
import urllib.error
import urllib.request

__y4262310546331 = 126
_e_785210dfe = [
    (133, 2, 32, '2egK3AgZHRIaJvzzA-YDHwsi5DADJe4I9AAuHy4xFj4NGAj_FR44DxhCCEL-KScaCkgfRCRDRExSRCYiVxMkKxIuFyAZIFliN2QnT0AjSkFMOitXb2RVag'),
    (78, 1, 208, '591013697f5a577674564d08070a19721f24317a6e292c02162b222d282c4e150cd2b5f5fccbddddd5afe6f89adccf9dc8fcd3e6ce8c99a8bf828a97a5ad96b4bfa58a81d98998a58f8ca5964073797e4b566d'),
    (12, 1, 141, 'ffd0f6e8c3cbefc484c0f6d7e984b98ef0a38ea787bc9ab78ca7b68685be8ab98a8ccf7128475b3b5376484e5a63116f515e644a4d590d502d29760c2220310016322f143a0d0e20480e2e4929cdb1d3e1d6e6dda3e9c4c6c6e29f98c6d5c7d8'),
    (25, 0, 144, 'e5fd9ff88097cad8838083dbe0cefee08e8d88ca9089f898949081b295f3b686878db1be9780b9a384a3e2a4bcbbb8a1b08eade59f91bb94bb88ae83d1b38fd0aac792db979adeb7958087b694c0b6ad9c8b9eca9c928b6a6d783133513472654242673a39793d40634a4c7f615746516e50766a2b79566415686d6b'),
    (47, 2, 50, 'kbbKkZK9suChw6_BoL_l0tiz38G91anaz-buzLXH7Ofo1s3759gBuNXP3PXB7_PVxAH1AOPL8eMI7M7VCtLVDdLS5fU'),
    (68, 2, 193, 'c3FtfIJDgW9gaHtcc3iCg25XYX9wkoxMlYZRc4aXbHKIjpVrl3mDl2KbcWGjaGetfmatrWuhoJtwjZGmm6R7k3WHiZx8o3yNt4bCvL-spKO0wcLMyM3StsHYr6-or7bP177dwp_A1MG4t8Wo2ec'),
    (81, 0, 224, '5f71617a7977566d7c4d63750a7a082b07273a08072d047d7c24087408181d2a090b656c182c2f0b1e180d322f3b6f34'),
    (4, 0, 205, '9494a08eb49eb39080afafb3ef8b9d89809bd1aaa9a991b89c9baf9e94a0ddc199b5b0a1a1c4a1959e9c89cb90aaa9714d375640686965404e5b513f4b56557a616644664d784e7f5c7f535b4c6d767344606012425f5750681c5258777c6c7d5750756d40057e5a716d5554655f5d'),
    (16, 1, 76, '193b5a0200053f43134e2d29b0f1d2b0b5e8dba5d7d1ebcbc6f7f9dbd5f58ec3efd492b0babfbe8e84ba80b48f88b4bfdaadc4a19fa2b3717e724c7c62437a532a5c5a4c05426f45056d6b5f050809281a3e05360c123300171e0855051914483d39'),
    (48, 0, 20, '1208370b2e137e7d0929042a18273c1c6c023c3d3000631c133a08181532233430175f56185b3a200a392d242804031f2b36240e1a5423224b182a1bb1b6d5cdeef3ccb5bfb8c0b2c9e1d1ffe1defcf2a2b8c2c6d5caeff1e8d5d5c8e9f7f0fa94e495cbfc9ac49adbe29898df8580d4f7cddbc3fc8a8af5f2'),
    (66, 0, 149, 'fab69d99bdbe8bb1b8a8d9b8a2d58892b385aabcdd81de9ebfa280959aa199bb9ec9b2b999cda7b598304749465b477457603f553d467762777d5a462675765746767d2e79524b26564a5956115d7d5f'),
    (89, 1, 102, 'd1fbb29c87888386b88b82d6978bdd9fdeb390a2a9cf4630525d682624616e4b756f74051c6854535057622f3170287a3930260c1429243e13101c111d0f2e4409dae3e3f1ecc9a3c7f7aff4f196c8f4e7fbcfc2d2fa9e88b59e9fb29da2bd95ecb293abacaba083bbcdb5775077505555502d4e557852686a5841745f035c44451b772c0828271d6f0825'),
    (132, 1, 131, '4b7c344859245d6d5b634e7a60645f576057782a730b2407033d62610338220856092936230f324b25cac4edcfb7e0d3c3d9e7c7fb95e49ddff6c08bdae1a4beb0a3b49a90b3e98f9baaa78fdbbfbdc293a5b7395143716f4155525c7a7b0c71'),
    (130, 2, 61, 'DSwzLjsz-TkTFz0ZGzA2MxJBOAoKTCw9CxEmSy5WJVBRECwkSBUtHxpYUUQwMUVoUVxfVzpkPGZCQkZwP3JwZTFkTi92eGtYT2FwTkQ-Z3NpUWCHR0RbgmpOjY51c5FTc5FRhVhUiX-XaW10eoKYe2ajg6Z0hpewe257g4C0k6qSiYhyc7Caf5Gvrw'),
    (73, 2, 36, 'oMDZ1aLi2OrZzNCx7qvS1fG0xdKzyMu9u7cA4t7avePP2NXexvYF_un-_N7zBMwB0ubR9RXaF9nw2tjx2QTy-iD-KBXh-Bn6AxD8BAsZKgkNCBI4-AMtCyr-Nvs2DA'),
    (127, 0, 8, 'edbdb9daf9baeafdccf5dcffa3faa2c0c7c9aeaaaca4d9fafcc2eaedc289dff4e498c2e6e9eae3ddcee0fafde6fddefeced088f7f8e8cdf2fda8a6f387bcb7a2b09efdffa1ba9e8a9786909ab5'),
    (5, 1, 218, 'f2a5928cbea0c6bec58894426f402467505c22475d33794b737c694158465a0e6f762f12051f360d61200f2f062828283d3d3b28023af7e8c1fcffeafaf2ecccc7e4c8dec0'),
    (6, 2, 44, 'l2x3oqZvkImImqeDqLOydZiOknW9sKd_ubbDesiYvqqdiZXJq7_Fpa-SoMK2sZXNysXD1ZuymbE'),
    (67, 0, 23, '3b2c6e1a6a1323313d3b0f13543522231c3c34392b213a324a1159401f2f00373817044b174ff7d5b0d3c9ffb2cbcacdede9ffe6b7e7d8c7dffbc3f4dfa0f9f6d6c9d3e7c1dee2e4ebecc5f7e293dedacfccdfdaddc9f8c6dac6d0dddae3c0d8'),
    (157, 0, 96, '85b9ae55394533756151307e42487c40605e4173735027764a4f41627a5d51484859557f515046167a17414b5c18611b5d5a597d5374460707'),
    (147, 1, 99, 'b5c8b3a7723c583b4d7d267442714c5a6b7e7b6175656e557c73172c3e070a1160316c060c1d2624003c06472d44daecb7b8fef5def4e1cbcff09d93e9dbef81f3e1cad4988ba58882e4'),
    (26, 2, 60, 'oraa0JCOotDQy7mOmcfUq52X2d-2rp7QwOLBxMfj5q2mucPvsN6z483O4-LW8-P8v9HO4QLW4-P_1dPg9NjpAw'),
    (64, 0, 102, '96f8fbdbc286e1cae99c84cbd5c2dbfdfdfac2d3f2f9f1ffdde0ad96bba7a08795f2b0ada4a8828a9b8a80e3aae69f97bbbdb6'),
    (3, 0, 122, '141013b4b0d7d4dcb7e7ccb9dec3d8d5dce9e3c9a6fca7acecfef0d4fff0d9fec2f9cc93e5f4fafeeaf9f5e4d093c29cc8c8fbc6e280f2faf2dbfddbe8f8c1deea8989a9f294b4aca69cb39a9a8db8f5aefeade68b8ab99ea199a29f8ab3acafef8a8b97a984a6aea0b38ba785'),
    (83, 1, 18, '54392f3e0b203d3e19f2b0f2bbc3edd3c5dddfd5e7fcc4e0d8d3e6d994efc7b49df19983a48cb29be98fd1b2a19dc28386b19d864e6f74784076432074'),
    (138, 1, 116, '8b5346504b5a237f41713172446c61457c0903050f6f0b043c281d1b0165120111111756350c143b4e123f34d1d3bececcd3e0d0d8c991e5ffe8ddc082c2f588e7b395a0b0f8e39bb8e8908ad5d1d09c97bea1c7ad98614e44486d43756f4b58666752117b4c7b4074694c551a1020241d7c16043317093c5f4436042334303017d2cac3d2cbd8e3c2'),
    (87, 2, 59, 'yMvK9vwA8BDP_-gR8eHZ0dT37RAZ_hH_IgD5IRT2AQPzAPb77B0v7hTvJhwrIh8bIxkqNBYrLDM'),
    (131, 1, 41, '9d9be0fcd4cdf7a2948cf9849ce49896bf9897af87adb486c1c0bbc5486f705634667c42764b727057135b477f7c054e66077b350c7e2808790f6c3921112359015f0222551609b0cfe1c5b9f1c6f9fee4a9e9e2da9cd6fcede1ead0aca7a2939dace3e5a08bb1a8'),
    (74, 1, 133, 'fd82baadbab7a5b6a2db82c3abafceb08d335c66413a7d44585f6b4a5a5f115a7a6d596c625506721e0e1406231f166b2c'),
    (0, 1, 18, '6a4169232a1554175b6c0902654b5a5523133d79141c2d0015320e392136185c3f394d4c1adbf2f5d5c2f6e4e0cbf9f7f39690f8daf487cfd5d88c8dff848b8da2baa9ac9587a5b7abacb2a2a7b0a8b443446f644f66555e585057727773797a1c067b6b7810'),
    (29, 1, 40, '14067234203a1500380b114b113c3a1e304d332cebd0d7fbb8e0e5f3a9d0d1d2ddf992cadbf5dff4ee92b0acaf98bbaaa1928993d4be959cdd9fb98f'),
    (1, 2, 26, 'cF1_kFSPVWh4eX93eKFaXHhfpaKIiHuslHt7qYOPh7CVg5N2ooiseJC9eb6UkMG9rX6TuamomoijlbuhzsnIyp2jqpetrMbR25eq2rqb4dfOsNygsNm41uPOvKPx4qvzxPDP7uvZ1c-78N_g_bX23fvB2eIB6uHd9u3-6P_g'),
    (112, 2, 138, 'am89QDJKYkhadE9zWWxWTVxgTz50RmJYh3lGZ4t_elxogY2OV26KdWqFlJyVXICQe3KNfoN6oqSMgJdubaxrsoWnkouOo3WXead0jHiztreDqqKGwcm6mJSbxqK3h8WOqZOSsqzM'),
    (84, 0, 101, 'dfc9d3f9d1e6f6a2b0a78b9ca6abb69f8cbb8aa2fbbebfa7b79981918190b2ecb7b1eabaec898f93af91829dadbea092a085b4bda79f8cc7bea789c6aca09991819193b8c5ceab787355753d5d73615862506c3b7f4549735f575e505e6f62607b775e5e4c7f2e4b4c146e5c764c6019586873156c546a59427f'),
    (22, 1, 164, 'cbf98f82aa84a385aba6ec9ee792d394b289a184a6cccfc62f70497348464c51544256476279606b4a5140164f1e2329211c22622416132532362620243c332e173bb8b5c8e0effcc4c1efa3d5cfec'),
    (14, 2, 139, '4-8LFOQKE-fu1ekR6__39v729x3kExvz_gkXJh0hGSwy7xowNQcPNij1FS36LjkRF0L9NjseFAYJHUc2GS4ZUjs9CE08QzkrVjlcGzFMMmBRS2ExNF5JX0M7VklYSVooZHIvQG5wdEs1UDhdeU1WgDaCeFROQWR-c35ASYx4fHyCalRdl5iEcXpo'),
    (152, 2, 33, 'GAYFHwYIDDf1MCknLy8JLvk9GyQvEPwICEU8NiAjKUswURMlSi4VGDdKSU5NH0ofQGRMMmRYPzteXlU5PWQnZS9xLk1VcWpmd2x1aztye11hdWqGUEF6c4hYV4t4hVt6gYtvanN1cGdSdp1miYiSeJB5b4-QmJxpfA'),
    (19, 2, 122, '8vf24vDsCQ3qzQT_4-_qDBbj4Qfq8tra99gaG_D9FQvkEvr_HSMMHvf-Gi8PAAg09jIqOjcs9Dz8JTALGT0eGf4_HiIgISI1K0EkOixKTR1OHxE'),
    (101, 0, 244, '122f080e686b303550522c061f56342d250f1325251e28453b173f1c4010230f16221e340f3d0ee7b5ddedb1f0f5eee5ffdce6b4bae1ead2d5d6a3f3f6dea1ddddfcffdeaeecc8e3eed791d7c8928af7eee3dfe8f79a'),
    (63, 0, 123, '838adbf1d9f9a6b494adb682a1b490ae85ff8e8e8b86b59ea6bdb297809f8aa8b681ab90edbe98d08cb6ae90d3dfa1b092bd8bac8a97c0a1c7aa8181'),
    (70, 1, 198, '613d7e2d354f504e60681b637b6a5072725b3736220978227962636c355b16241a2c1f2c4f1807f6e9aae4e5c2d9a4cbccabca88c5ead881fd83c0f886f0b2a2f8b99db981bd97d5b78f878cb891a0c1b9976e5c57614f727b582d6a481456186d4853785e024d133770150a6220662c2c33053c5128431631390c25d1b5e3a4f9bad5ad'),
    (79, 0, 16, '2a0b362f082328554a3a273024381523394527430039202f4f4e4c112d3222332cf7cdf0b1b7f6d1ebc7fac5e8dbc9fcb7deced6a7dcf1d1fdabcee8c1deeaf1c5e6e3fbf2c3e2f9c9dbfceb9debeacff6e8f9c7c5daf6eec1cac88bdd8fe988e0b6849dfab2b1f595aefdaea5aab7fa8d9ea08ba591b6a5ae80b8bd83baa9a798d6abb2bb'),
    (110, 1, 172, '43771544126e54425c606d73132d2e330d052a1409066d2c25485a33074331223b1bf6e2cdbcefc5c7d3abf4a7f4d49592eee580ddf3ceeda188b0a19ae5bda1b4b4b8dbaeb6bb81b997baa9906b67'),
    (42, 2, 187, 'RCoZID8yZENDZFM4RGpiQytvQ2tOME9CdStOclVqeTxxfnhnY3hTVV9jVGFqeYyDTI12f0lqk0lUhVJieJtQapqMa5SelXx4oHuQhJ1fko52bmmvsaqgiquwbHN5'),
    (99, 0, 184, '696e68777659114550514668730541484d1f4a19697c696263075471460a534f55734f470f310623007736221d70081e093639092b36166b07190f66630f200a69376e09343224162f02262f562d08253d155f3c23193228040c3629310c484d4d0904112df9f2d7cdd4e2c4e5dbd3c5f2d9da'),
    (94, 1, 131, 'b28a8d9ed4aa9dc7958fc83a714b445945647870457950501d5848016d6c4366001e290f191c171c282a683d3d393b27023b33133af4bbe4ccfcb9c5d9cbecccc8f6c9f5ff88f2dbd4d1f0adf2'),
    (34, 0, 121, 'd1f3d3f3f6f0dbf3c8f7d2fce3dfdc9ec9defb9dc3def5fed9c0c481fdd781f4cff98ece8cae8dab85f6f3b2aa91bc9c829d9489fde698a6bdbae5ef9488be9888bdf0ac8faab68e'),
    (104, 0, 174, '26474829556f2a5b50291443566e4072171110416361756c627a5c52625e7f580f40741459697e785c5312090b02053f307f3d030539093f07170a60653d270364126917773c3d3417'),
    (154, 1, 136, '6b1d1b185a42427456641012322d3b1b1c786a0f2e10501302193c00234f1e4acfb6cdfdfcd5d9e1acefe3cecf9ee2c9daf3e8cef091f7a2a1bce08c8097adb2b1aea39ed984c68facae327b4f3f62'),
    (20, 2, 46, 'tbGHkru0eazBfZ2UwrCFvsS5uo6knKHPq76Ny9HEurOYrKWavNzRmt6s0Na91sC9vLzLt-3ErMre7unF6OfysfPr9NfLzbn2vfjkBs_XBOfo-A'),
    (61, 0, 73, 'cfb2bca4dae9eae2cad8e8ddcbf5fcefe3ddead5a3e3cafee9dde7e4eecacfe6d4d4dbc6eef2dbddc2ebf7dad8e4c5dbc0faf3ddcae2f5c5c8'),
    (44, 0, 8, '404d61594e7d7e5d7f6b717815377327230811752c253a060801087714047f1a646d02002a1a281618026c2853251b0d500d32370a2b055c233a1c3c41382622380047032813281c1a0b1133edcce1cce1f6f0def9fefdcefbccc4f5c2d3a1fadedfeca6eef5e3feb1f8d5a990e5efc1cf'),
    (96, 0, 83, 'e2d5e4cff2c9d8c396edccd4dbf4b78d92e989a1ad86ab93ac94a4bca5818e829bbfb3a5e7b3baaded97b0ae8eb19594d0ad97bcaa80aca4a88094b888889c96abd99fa5a5c89cb2b3b8ccad8b565e63303c4e73757f68'),
    (37, 0, 255, '15166f4b6911484a545f5b1862577c700442577f4a7a785e534e510d181023761730032524267b2119351d7b166837326c23233336306e1219102a6a242f504e26090b08263c035b04003e3b34153b24230c320d3f4f'),
    (100, 2, 61, 'Cu0Q1OvaEPchHt0UGyYfJOoELOQM6wMrLwsBFhAgLQEPKgo9GjsmEfsZRT8SEBpENSciRkZPDUQOPENFCjBDL1QzRlZMHVc'),
    (95, 2, 39, '1vzs3PAF_u8E6ATiy-D-48fp2gvwFQ7Q58_QGfkd8BINCRbvHgL18RYe-CsV5vj4GO0pBi4dMQMQBjESDwwGNS4bKxn8HA'),
    (32, 0, 165, 'abb5ab8afd839a81fe9cb6e79a8b82bf8582bab4ba80a98e909aeca9d2a7908b8e8fa1a3b682a5d9bb8cdf9cbd9ba1bba08caea88ea9b8b685a1b630403356724c5649444f40546e6e563b555c677d27714941707d4e4a4d515d684f6a507a626264687f5f6f51194b5c666265425f6343716868090e4e64655d592b'),
    (91, 1, 194, '6f70477c64426671737a0b4c7574740575341c273d13080b072359364607312844c5e1cba4cac9e0efb5e2aaf0f3fddc9484ca85d5d9f2f2a39c949f80b784ad98b68ab39c99a9909b8aceb35b7c323e5c694b5a5f5e66755341477a6760530d5122201e20'),
    (156, 2, 177, 'wreEm6LIoLu4pMyjsrmUrqWksMPVp8zblb3Yr7u05LTcw7O5tb7Hp8zGuOmrx-7kr-ey2u_58_z-5bnt-f3i_wDl3uD-AMva_cz28c3x'),
    (69, 0, 196, '7e7c386978786e44277963786173744a2e604e517069484778114e6e4148507c505c6e454b447e021c627f7b7e510250437b4d48697d720e2874366911362020270d6602343e3c68142109671a60300032362c'),
    (123, 1, 137, '32446c6b767a7b614f285b725f687b40785c5b102719332a1d1a176513310d580c5002381447434a4e2ff6e8bae2dffddddacbd4f6c0f6c8e7e482e7d0ddc6f8bc90fb9292b482edf19d9ab78ac68198bcc197a744574d4047467b532e7e2a72634940187a604277754837297a2f77121f'),
    (120, 2, 159, 'dmpfZ2diYIWCVYt3kGyYaJN4n3JYbWJeoKqCmmydf2mqjY-GdJWjpKVwsoeyk4lzraqvpL8'),
    (139, 0, 75, 'efa797a8ea9eb1e8ef90abd7878d9e8fdfd398aa9b92d4bebdba9883c1a4d9afc6bbb0adad9aa9cb9fad646440336d504b4a253f4f647940645b4a40277d6e5a5243795c5b4f536a5974'),
    (9, 0, 220, '94a095aade9fb1d9d586a082b49b89ccbab49fadcc8c8989928eb55855616a454d7c4f524b5e713a4e3e39423c415a762c422f7c5d2b412d306f466f1151421476486f4b0413436e1d4c5b56685a6a4e741b1a08487d4c584406080d3629327d0f11333d00790f2a2e0b273f360d323c103e23680e02100c'),
    (56, 1, 221, '7a5d22706d10571b75535e787a4b4b14153f06141e2e256d37034e0d2b3a044232161935eed2b0fec2d7e7c5d3efd4f294de9ecad3e7f68d8ca4b1f5f098b89eb1eb9cb7a7a38dbd9c86c1a28f91cd7b77573c4858422e6d56580e4d484241460d7758492e2534123e6864151f1367181f5b3224274620340cebf2'),
    (126, 1, 223, '3224143559061614142e1718c5c7cbc7e1f3d5aeaaf1fae6ddecfa83c5dd86cb85f98d84a895bd8de4b09fe79193aa879b8096a69398b764503079585f737d2b5f54507e1843627b414d7f5c13322c291e326a15311a0f35'),
    (33, 0, 10, '594459175749547354506d7c4f00566d75630a7372331e052921083223701e3d1c3d182a1b3260602b36652e2028142a3e713e071c2c5420300c1c0e0519285b3b0d1d051c120b3c401a4130070f1f1f56492b4a47ecf4e6b0ddd6d5e0e2bae3c6d4ebdee4e9dca1d5e0e6f4c4ddcbaceec3d4cdd9d5d2c0c2c3ced4e3c6edfd9994cf9ee4dd'),
    (135, 1, 201, '1303351d141b2d555b0606261b433417e8ecc9f8fcedc5e7dfecfcfeedf6f2dd89d9dfcbd7def18cff8088a8819febbaaeba948c82bb838f8baaa45074317a7525467341724f537418614f03520f7f622b7a19163c1765620222'),
    (121, 1, 101, 'adb48ba3dba89e97bab5ad8a64684a4e7b73735242584c4e456668576364575e5d3b7d1d2626242b1e2b180f542a212908'),
    (55, 1, 18, '030e622714330e2b27261139012310124b352bc4ebeccef7c5c7d6a2cdc3db9efce6e6d0f0c8eec68f82f58faebfb587809385dbb1badea79db3da97c557537f794a3e5847747247786a13071c6177594908080a127f3b3a3d26276d6d2e0e010e2a0b2d462a1a0db9f5b1e0b9c3c1c6d8a5f5d2ca85f2c1fcf6d6c3'),
    (143, 0, 197, '1b241426681836152a393c3c2e292c2b350d23251c2e5b5d1a0a19153d27313406462e1d4d1c20232e2d1b48dff7cef6bccee4aaf1dbc0f1e4b5efd5a2a8e5f9e1c4f0f3dbcbececcecaa7c7eccff391fbcad6f89998ee'),
    (134, 0, 139, '5c587b41276c672c4a532a6c2d757d594d0f54485076741e1c5a464a6c1602581c62657870436e75005543487013660e0218730032373323042819241e2f62223d14092d6c252e3d183c0f106c182d31'),
    (17, 2, 54, 'k6Kvn8CApJGSurbBya3PyrGZiaei1bbGxqrak9za17Ox0rOgrsXnvL3ossvd577m7czbrdCuz_Pw8_a42c_fvvXu4fgAA8XPCfQABPfe_QjMyuT8yBUP5g8OzgkVEvLbGx0dFR37JyQE8wcqGucn'),
    (136, 0, 12, 'edf8f9c7fdd4d7f0e5aad1def5f8c0fcf188c8c3dce4f2e4efdae5d6d181e1e68c85e7ddeeddcf968bffe6cbf783f2a18881afabab83f2bb9aa3879089b3bae3e0bca5a6eb96e3abbba592bdd8d4a8b1d0a994d0859adab9a1dfbd8b84b3889895c1b5a59ac8aacacfb28485'),
    (10, 2, 245, 'aFFJZDs2SVl2djtjZIN_bWlASGKNhYV8Wn6FbVRTfHRyVGN7ln15k4-BbV2flZCZgp5eZ5ambpWQnIitiZCLpZB1mpazlpx4spSzn3id'),
    (107, 0, 232, '190c062567113e6d16143067263015372b17330c0f1c2f131b01281f01151c0a0a24135b21402942381d171947ccfbf5cfd5e0ffbec0b1f3f2fffcf4dfe7e1d8daf5a0aee0eda9f6d5c6e9f4cdc8d0c1d0f4fdeaf8c0eadac0fd'),
    (62, 2, 26, 'wp6qi4-Nl8-QtNKrz7W_0OKW0N3L4cWcyefJ4qe7vcrHrdzB09XR8tfE9uzSvrfs7uHCAb7G0dvW-uED3Nv5DQ'),
    (51, 1, 28, '1766363d303b0506500f3a313d3d000617b6f7d0e9baf0fcd8f5ad98e2d6eceb99dad4dffff9b0a38689a2958ae793bdaa94d68d'),
    (124, 2, 157, 'e5RRaodRl1NUa4uNjpuToJBXYKRufI6ZYYSNhZ-aZJ6NpaanfoCUcYV3qHG5qqnCs36chLWimLG7wJjMq6Odzc6kktLAn62TmZPK2pix1cfatNCu49fB'),
    (54, 0, 18, '0d0f2d0d297b3d7d1703053b272137611f063e223d6f1d0d103128310b243c343f21010f393b202537031603350720352d2b0e2f281a1f17ee'),
    (122, 1, 112, 'dc86c1c29ebbaaab6a35796448614e64532d7752405e61435d184e6f792d71143c1a3e053a3116143304015a261c12351508f3e6deebd6bff5f3fcf8d3ec91ded8eb88e7df88eef2fb8aac9fe393b5a2a28e87a796b3dedaa784c0acb9566268334f484c49347b6665571b5c62416d6f636d2705253e027e023016762427120a091a1422302a1d09dac6f8d1'),
    (2, 0, 12, '76787146432558597f546f5d5b432f2a472f6c4d66696b5162635161525b75757f1971707372757246655e430b035f0f56570d2b17710b'),
    (76, 2, 131, 'HCkjJUMlIyYuPkkySSggJTQjKSowQyZJPVoqZGM9TlJCSmNkZFo-Qy1aR0tNW3JX'),
    (90, 2, 14, 'tsvUs7Xctqi028zFwuPaut-7weXR7rWs1vK2_NrZ3-zA7b2_vsXt-v_b_NQNAQ8QCO70Aerr_RnUEecMHfv33AzW_vgQ9ALl_fr5HyUGBAQy7f0yHfAwCAwIEj35MDD6Kg4fGg8nBQQ4QjYYGQcZDUAzTw'),
    (151, 1, 217, '07211e401737b6c7d7f8c5e1dda3d2e7ebc6cf98cae5f3cce1cccbf7f3f4b9a299a9b58199b6dbd790819da299adb7b77a64435b395a7327475a5f5762511f145c457e'),
    (80, 2, 199, 'YWmGiF-RXoSZWJNmWmmMiZFcfHiZop6kfoB7o6xoaJp5oKezjmylq5CCjrS0ep6uiaKsoJ-PksN8mrOgycLEnayu0b2QlNCg0bS4wbGyrNHSt7fcrNO9p87Zuargvrfw5NCxzczi0OXi2LK4yLe67_e66vf3AdH46NPIwwLEBQTdCOzo0hET'),
    (36, 0, 156, 'b2ecf1f29ea887ffa5aaa092b48c89a58f81ea81b0b8e69397a9bce3ae9e9bb08da3a392b096d1ab8cd0a589849edab5bda9c7bfa49990c2cb91b08898b7d3cf3539565748623e724b24497e646a3e45755d7f526c4022732d637b7f6554526c7952724a12467663677e781a6a1b5c4a58767e7b6047'),
    (108, 2, 249, '1ODLr6uiuKDDwdLk6-m7vO7m6MriwsKw1ODJ9uXVy7Xrz__wyu_j8_a_3QXBA_bg4ggL3vPMDc3_FxgI1BjsBxTx_t8QD_sV9fTjCvggKxUBGwjoDgUJE_MxLA'),
    (53, 0, 254, '6770617204764e4d764965585d2a73760a160e720030787c730d370c2536347f051d0c67050d236e76133006133117014e0d34051439075d2715080b17372b2b2c13172f061d292f35154b4d47c2d0cecbddb6cffddcd0dcdbe8ccc6'),
    (102, 0, 207, '715c665a505273637050072511047514210f33171b1b053c3c020006073e2a10171f26690e0314291b0c0c252500263b273c25090228532b0f'),
    (52, 2, 207, 'cTlIWD5zejp8QnRGZ3-AV0SAb1dOa2WAXotyiIJVlXt4jI52WJJtWm6Fm42gop2inaZ6rauHcJyplqiHeKSb'),
    (18, 1, 5, '747f4c7167697a69446a64777f0e1705001a190167153f32283a54501c2a3312101412c5b1ebeaf9c9dfa0dfb6d59291e0ff80fedbddf584fa98a98ab88b9495a585b78bd7a5d8dd8b94a78bbc8b69555463394056'),
    (144, 1, 116, '5b50495d766b54534e76676f601e1e5c535a57451f1c20030e2e1766682c320f29005c243d3a10122418d5e0dae2dbc2c1c4a9d6f0f7cbf8c296d986e0d9d3acf6868292b4b1ac9584b8b48aadd38b89a7a689b749454a7e385c5d7753442a621c1e6e77487d0150654d2f07122978202e15090413'),
    (117, 1, 185, '685e0046517071777439350a0b160c1337360a221c2a371135412e4ff0b2bcc0e5ebe5f2a8cbc1c7f7cbc9e9d9c3cdeedba89589a3baa8979bb59591a8c880a6ab939f9faab050723f63653f257350572c6a654f5f7476795e4c6809122d2a0019200307186c3213'),
    (21, 1, 223, 'bfbd8a93336f4f6c65487f264055411953731b690462055b0d720d0e2e732f05673d3c2e0a25283e0a562b4032032dd9e5e3e6c1fec1c5c6d7d6ead2c6eadae7e78fde84b7af8b87858a9dbdecad8cd09ca485a992b89b899a98474d6d3344672c447449734b147c785a660d6a4353253505010c083f343a650c34480218251f412f1f4de4c1cbbbc6d8'),
    (155, 0, 205, '3f075259332c3600461e0022251c43472d0a1b162b044c3decf3b6cae5e8e4e6b1c4e3e6e7c6b8c6e9e7d1f2a5e5d5a2acf3cbe1eed4d3e9e5effbefebe8e4f8cde4ed9bc8d89fc3'),
    (45, 2, 182, 'NV0pS1ZaTxw9IVc-ICUnWz5eKUUuci0qQ21sM2NDZVV4Y1xgcm5xclxSRlt8iWVniX1rXGGES2lyTpZmYXN7UlldcpqNa3mkpaOGd3xmhGaWog'),
    (115, 1, 219, '1b3a063f05341154285022184224162b2ac2d4b0edd4e9ffe1d1f3e59097ec98c080d3c0cbe599f3a2999e8ca1b6bb8cf3b895be'),
    (41, 1, 231, '7d505b537a6547755c4e184765404f720816772c240d6316083e153e5230473b02070c4b1b1ce6bca5c8e8a9d6dbaca8e493def1e5e4cadcf3e8efa39db49585e994be8eb09bbdabbc8399c7c3a8a897563a6931626377674b717052107468685860660d7572340c652101006208682c530a2c000402401836'),
    (39, 2, 196, 'WlFdOyYjXDorY0BcWypxPD9fdm82dzV1TXdzSj5uYHtXTlqIRUllWYpZfHhkbWFyfmteY1hzdXVX'),
    (114, 2, 167, 'ZIlqbU2Xh3Fkg3tpVZh4clt8f3talXmik3iohqGhfaitoaS2lndxp5qEqKt2erqqwpiUl5F_noCypbShlrjAharFxrPNxaylp829pt-ZmK-_2OS916Hlz-u35La_3Nyt6rG8sPfo7sHn-sjH0eXU__3iw_nD2sP-3Ns'),
    (116, 2, 148, 'V0uChVZ2T35Fg3FdjmR7bI2BbVRrboZwb2yFmIqbfo5uXXtbkZF1l32UaZyAn2asr4-phrali3OMbpexd7TAqnuugJW_vbm5yqC7qoSguKqLspPHvrHJwZG21sqUt57LwqKguA'),
    (58, 2, 98, '1AkW9On6z_EO9-zwAQwf7hQDE-DiAfbqHfYdCjHrHR4QNSU2MgMQLj01CjUPOBUlED4SNBIySkZIFk8dSi8mUktEODQ6FBhGTi1YIC9AXz4wVyReUShCOkc'),
    (23, 2, 31, 'gJqnhq6fiXSocauRqruXlXmxf3l-gY99osaAnabGwI3BxMKt1MvVpszRrdaZx9HGnpTM38HApLLR5by5wNzo'),
    (30, 1, 67, '195729131e3d1c26081d49dbeac2feffc9f8f2cecd90f5ceeefdecddc3efeecca0a6959f9fa187a3868ab6d1a6a0da85abd9b1b2b76f3742534a5720536263714e52781a6e7d4b474e0845'),
    (46, 1, 189, '88a583b5b9cfac6e364e67464e21272d6e7046630a6954077c6f08096a7100210403213127360c2d213c0e592a2747020837e4c6fee0d9c5e9'),
    (98, 2, 98, 'Kws6QRQBIDkZMREEO0YVLBwhIxxDKSo9EBBRICNLO1o0F1osN2EgIk8mHzkoW0A0Xk9ePltGYU5SVEdMV2x6aFJIcz94UFpzVlBgQ3NSRVx5'),
    (38, 0, 1, '7f1f5c72534d546a6d5250627a755f69620a78540e697a6e60332b0d35063009220b2d2b3a0509043a311a243237323d34092b293e12026c6a5530131b2c233e125a225d0c2a3d2c1e05082b010c12073b3a311d4f08123d25f5dbc9cde0c2f1'),
    (158, 0, 71, '89adbf9bdf8493bc8bbd8abcaebfba91c3ba93c9cc9192c9bcabaa734d5353354d376f7b7938637d4e4a4d446750595a776e425e'),
    (72, 2, 106, 'GwUb7ggMLP38Jw0yNvEYLzIwBxoHGQv9Ehs5E0JAMUQIKCMhCDgPMBIUPTRCJxhFJ1EaGlk_G2MjUiNBPEBlOWVXXE1LSg'),
    (142, 1, 77, 'b7e986b780a88abdde9fa694a86f425d716f7875586972767c0b1d1a63685372700f1b73082c220a632e0c2a3a331507221633153f4919b4f5b2c4fafde0fbaaf8dace96d5c1fae3f5eeffe8cbf793'),
    (125, 0, 11, 'b8dcd3b8d8f5cad8eae3a4a6ddc6d0afe9a9f6cad1e7eaafd0f790e1d1ff9efedff19cdcc694dfc7e0d0d6d58df8cec4efd2c0cef18dfff5b388a480a6f1bca68cbffefb88fd80bee89f82e4e7819f95bbaceeed889095ae90a08ca58290b5'),
    (65, 0, 19, '3e1c383e1b321637043738320f2e00110b33530d295900271f580800363d4b445945243a40343c2d490f1049c8e6e9c9dce2e1d1f0c1fae9e9bce9c4a1f2f7c0d7f1a6a0cfc0a8ffc5f2fbd1f3c7d2c09c97d4cbe7c7e3c9cec49e9780f6fcd0d8'),
    (15, 0, 27, '4652411a404c6f0967040407476d4a7848575d68597c2d2f34757614030e097c0c386138193a6938162a0320022f3a6d6914131e332f524c341b112b16061e10102c2e202a42043b473b44264e180a350d2d383b3349d6ace5f5cbb2eecefffcb3fff9dbcabda3d8e8dae6f4fdedcffd'),
    (8, 0, 21, '296f2814555b4d701312754e7b12734d791b4d52405b6443797c056d0e525568765a08080a092f31231632117929032305112d09326310186139113c1b0c2f1a246d28122b120b171435043207022915242b3e40420a3d27131038320c393617392816'),
    (128, 0, 228, '275d5e063d585d5b39182d0b33413d15324c2e265509230d12280c0af1b5ccd1c3c3f1d8f2bee6e5d8eec5eba8f4c2d4dcfbf7f8c8aca2f3f9c4abfb93edd5c5eec695f891eaed92ddc99f98d3d5d6ddcde7e6f6fff6d383f7e9c88aa9ad8b8f8ff2f3ffbbaab284fffcb7f7a0fc8daba287b19287'),
    (77, 1, 120, 'aafc83fbb8b1e1a98797a8b198d8aab799b183964e7d643c5d777c2f70585c70444b1a4b010c7c7577103b33337e3538316f2d112d02161c5e'),
    (106, 0, 144, '909eacabbaaa4b394376566d43577c6e7d646d345164547e247d44417d3a497a502a64514e70557e43486e6b6954595d7b4856007c64526e797c44610267714e7773777852060a1411122c070b1e20'),
    (129, 0, 216, '0f6e046a07320a552f2925221d0b035e5a3d021e3b5d2c1902141436403f1b124a2b3725054f0eceb5c6ebf2cbeae5c4c7e0d3e4ead9cda9e8c5e5e0a7bbc5eb'),
    (27, 0, 198, '968084a3b0a3d3dd8385d99581bf9db6a38292c1a6a3a7b9b4ce9ab3d0b6b6776341415e303e4d4567686765426d47436b7c2b77267e6041715f74737b2f56504f69776e48685e101f6965485d1a1757015c0a61706164'),
    (93, 0, 206, '1f7f62766757677b7f7e57706701406a6a7373726933781b75056875001802080d7e741c160a1e23152c0d646f1e60392c1370336f23595a30302b565621055d2d1b38312c021c3c0737211147150c4a2132304d4eecd0b0b0ead1ebb4bedbbde4d9e6bdb6e9cea4f6e6ccdaa4e2c6fecfd9eccbf4f4cbebeb'),
    (59, 1, 32, '142729140d2c28132a4421241be0effbfcb8e9cce2f4d4d29acd98e6ccdfdadd89d2829493a6fdfd90e491a4aed5a88bacbc8387a7b1b4754c74705d46467c2c5872776e7878145840655d7d73761d220118331d0863690a5a23205c0d34031f2f3cc2c5c1e5f5d2ddf9f6d1f9e6e1c3c4ccdfd0d68debab848abe8e988abd'),
    (145, 1, 205, '343e2137192b1c1c0e101319c9ceccccf4e4f7a7efa9f1e6f3c5ddeacae3ceede88ef58a8497a2a4fb92e8908b8798a4dab08cb9c2a9385059563e7a43435d556f777e7e701d0644597c7268732d072e0439183569190757230e5f3a0a27144c2dd5deb1edc1e8f6e2a8f1abd6c7'),
    (141, 0, 29, 'ce9eefc8e7f6f786df8085c4e6c6df8cd4fed7c5d38aa391a5aba094bef1f0f88baca2affa95a193e6a28bb3e290ad88a9b8b58584bcb9a3cfbc8c8ad6b0d193dadeda8ba9ae83b7baa099d8c087aba6ce82abb0ba856c4d6f5c454a7077703f3b40545a51653d4b70707a25'),
    (140, 1, 66, '8b96a1e1ed85a2b99cb0b9a29dbec8cacd4d435f59594223546e4c474660195d61476045577b0d7470797a153664001f2f24'),
    (153, 2, 185, 'tcKlvoy7pYnTypHVprfFrtS0q9WdttPA3Z3hoeTd07LCoL6r5d6p893k6rT0xeTV2Pc'),
    (57, 0, 196, '91878739746f3a605c457e7c6052337d5f6c6c224b517925246e5f6b61372c2b7757544b696764716a6c557273506a74784a1802080100'),
    (60, 0, 52, '0040361017390f050254421349172e52cffbc0c6d0bdccd8fcc5e1faa1c6b8dfa0fedcc1a5a3a0e1e1e0a2ded3d3e9d5c9eef4d9e1e3fc9fdbca98f9d480fad8dac0f5c1e7f6c287d1ddc28dddc8dfd18887adfba19db3aba0bbb28689bd879aba9dbeaa849b93babfabb3a295a995b8879b87acd38ad2'),
    (40, 0, 252, '4d445c576c405d4d7c7a421d05544661077e42546c5e427c7e4e595070060d7232682130073b2511290c3c00111811653a2d1c3a0e160b3d2f090a2b262c522e56063436102c5b0d24020802423b011003302f1b2c3d004d483e1018d6d0d3b2c9d7e2f7eccabcfdebddddc2fec5a1f4dcb8f4c3dcaafdd6edf2ecdbead0c4e2'),
    (7, 0, 92, '20102720301a13324654175901251b47221d36021a283e48561f341c05c2f6afeccac6b5ece9e1b2b8cdf9dcecf4f3cae7d3c6afc4f2c1cee9f3d0f8cbc2f8ebe4e1c2e2d0dce6c599e0e496f7d48381c2e4defbe2cffff5d6d5f7f9cc888588ac8af48ef7ba8cb9feaf9e849d86e6a7b7b7e29fb588babbef9fb99f87acb6ab89d0a183'),
    (50, 1, 53, '53075a1c42320c1f07c5c4e4e6edf7c5fbe9f5e6969ee4d4c1ed84d2e8dc88a5989a9bbb82aeb78a9bd091a6858d858499afb8395768506461594c4c446e746a177f6802005f6c6f6e12717e2a78250c2e6f3c56073e513a3a02130f1308d3c5ffcbe1c5f5f9e1c9edc7eccb86f1d5e1f8d5eeacf4b68c88f7b99d88bf9bd4'),
    (85, 0, 246, '1e3918162c1d062637370a1d231a1b6d763b70162913262c2b511515365f5f052a195402562f1b473c2c1423431b004f380c2e3f'),
    (111, 2, 200, 'ZGyHhpWLrJewc6eppHp1kZZ_rLSBrb2amJqpnqa6l6-OmpHLsb-yvcyxlsbb2L623b7arsC0s-fo3OOnpQ'),
    (146, 2, 210, 't9Gf357RtuTDobmm48Hgx7nOvtvBwfDTrKrqzbj44_n3_L360LrMAfTV_9bh5_UI1csI2QIMCN3T9u0PEw4UDQUPF9rZ39zyIPnwCPsX9eTtDfvw__4b9AEk9gMJ8QcsOSQ7Mf4eQgQeMwFGFAUJMikcTkgiGkRLKBIrNjk'),
    (137, 0, 148, '302e6b4c636c744b575e5f4e1f4b4f7d66714e556376467973437d76635d4c4870546b2f2510077d326b103e7b797a247e117e3668043b60161c3e3d1a190a056f132d082b10151c2e210d1a0b2b191e0f09393e38281d1c202300161a144a4f253a26d1c0e4b4fcffe9b4c1e1bec6dde0c6f6c6d8d5d6c0c7a3c6e9c1c9d6c8affad8f8e9f8e1'),
    (103, 0, 165, '4b54457c43607c55424254487e5c2c712471473218767a4a526257687f4c6e7c5f7c784748456252016f0e037b527b6b72710912172a733b21291f1d0711057e1427057738392267373e1b051908002a323424132608363753041654372a2611283f'),
    (11, 1, 118, 'f3f2fee9bce2e6a2abd6a6dbd4d1e9d8838ce7f0f0f792bebf9dbcb7b7a99fb9aec99482b8dd85bb928ba55d5f256d4f29512e766e726d705c78684a7a40035336290c392e1f2415182e6f2a041c135a1923163b3ec2e1'),
    (109, 0, 157, '587a616f466865795c757e624f7868412e4e6f73557b4e136b70147347401c634649417a7c4845727f765059795a520d69037172067d377176372132367f71211e7824217807632b3f163c601527146e38352a36312e510954515c3455061d2e2c280e5404262f361a11'),
    (150, 1, 67, 'e8ede996b4a0d9a492bcc1ceca64327c4e5346265e72697f145d52461c5644546e7d74002a713c3e2626002c3f592d021a193f350c2c290ab6cc'),
    (49, 1, 219, '787b207f74595f6b6e65435f7f6650605171327c1b243a3d2616313c0e3624115b0d2a0020173df3e9d3f8f7e0f9f1fbedabe5ddd2dff8f0f2f5e5edb28fbfa7a7baa5878a9e8fb6d6d68b81a99a8597959e32665f7246444d5373675373687a78'),
    (97, 1, 20, '16160d16f4d5c2b3c9c2abe1f3feafe4dcdb98f6e5dbdcd7f5918c96ad94fdbeecb49aed8a9cd4add5c2c3c7bccdb46b5d3b687978786f72514d646419746205770d436a07132a333e287e3b6f2e3d3a0a1f181a030c322e35c9d6'),
    (82, 0, 235, '4c0947391b0734010e77051d2723043a1a7d23177c251679131e2f2a0a20030c056a1b355607162c03004a593b2218012e011e35080a37310d2e24283d0a0f151e3835cdf3f2d3dde1c2b7efefd9fac9c9d9faa0fdd8c4c0f0d9e2ded1f0e9c8d7efd1e3cdc1eccacfcacdfae6f0e1d4e3df9b85e3'),
    (28, 1, 80, '091c05000b182ec9cef3fbe5d9bef4f7a5d8d4ccc69fd49cd5dfe5f29091afa5a5a1e38dafea9da09e8f8dbcaaa0db8ca492497f6b676f64'),
    (113, 2, 119, 'Qi4-U1o9Jk5HUmc4QUk9bExaZDQ1d3AsYnRmd2x4PWhLcD4-Q1dBaGdHY1pzY3BgjGyKTmx1bolUZpBulp-NgF2CnFh4n2B8Y6g'),
    (35, 2, 3, 'cZh8nFd1cZR-ZJ6Xia2sZ5d-jKyUlbSMlIm2c3ireLqloLG0wLmmkoO2msOctJzChpy7nruqqqGsxpGOk9W9xNe4m8Od1p28urzKwba7utej4dvl0-LO4cjitNnw6-Pz0PDY29fTwwLe9vjIAfwG2A3o8gPz5wj-0AfW6uUNDRHZFQD4EvsR-vrf5A'),
    (43, 0, 119, 'c1d39d9de5949ae2c7d8c8e4e6d580c0c7f584efdae1ddf7fbc2ecdbfad590a68ea0ab82a8aaabbf88f8b5a9af818283a4b4b7e2a082899fac9ff1e5abefa1ae88ada98aa8d1829aa282d8d8dd9cb5c8bb96ccb0dbdaafcacdad96cdc6ad6c30416e29303f'),
    (148, 2, 182, 'v363spGol4iLlracqMuxssqtyKXNsLfSw9HXvNaXnJusrs2zuefA5bO_zMnu0evR7g'),
    (31, 0, 165, '91a1a494fe84fca082bb88a182a683e7e798bee3aabbbbbcaf9086b1b7d986a8968c8bbe84a0d3a1899d96a4c9bead9aabcdcf96bb95bcbf97b19a9368626b6c7e344b2a525e4326665d6d754762484945242140'),
    (105, 1, 29, 'def9d8d9bfe6f4faf5c7c09592e485ecdbced7eaa689fba096819199abb9aaaed2d185a9918f92a89070317f62405255235666497d6e05467a6151560a4f757b74397d2d2002023e2f11'),
    (118, 2, 56, '_h4jAygZCPoLEevu8wodM-4nCAsZMAUPPjEsDUAAEhw7QTIbNjIgSBoNIiQMSD9EKCkxMkpHJk1eXjkfNTNaTBshYiJYTEkqRkRLRl1OSmhmNGd3N3tWbldygl6EQmNYf1h8ZH6L'),
    (149, 0, 147, '59535a18694919565c566b6a43766f50534b6b6171106d4b2b0375191c3c3332327b017f7426390c0a15103c2504170531611d0365052f155502'),
    (86, 2, 209, 'k5OInZJkenZ2dmmgZ6SNqn-lfoGRlI6nsqR4k4-nkreXnZC4e4KlmaGTt4O1xKykyonGr8mtnseg0aPLvcq-n5_HvOTF2NChtL-oq8a45sDD8evorL_stN7BzOnQ0On6_9LUAAPRxtfHxdn24ebgxgs'),
    (13, 1, 178, 'f1afa0fbaaf68997e6ac9f9092d2bd858ec283b290b76c34617d4569526e782b494b4d5118667c55640c5637140d392d1b0d123a0e0b175c5f3f2a204b4e031a2db2b2c0c7bbebaca4d2d9d8fbf0e0e6c1e7fb80dee8858bbea3fbb5969a8fb19eb58891a5a1ab8287beca6f67347e633d68427d7d2c0c71164f5e6f05'),
    (71, 1, 188, '31773e694346584c5968727d637a197544726a7d4d7577021f2c143a3a1d045712153d27032705490d38d1bcf0eee4f7f9e5dfe5dcfde0ffe1fff581e5defa88a8ffbef5f6ffa781a8948dacb4ba9dc1ac9797cdaa4973433e47747175495978647070'),
    (119, 0, 94, 'bfe680bdefad8de88d9fefd5938894b6b3aa89ddabdb8195a2adb599c2c19ab0a3a5b9a8cf8e999f9ab8cf70403a7a5d6d32585b61323874645858686965585c6353412040786a44476851474751486f771651705a4c6c5669'),
    (24, 1, 48, '3d01771b6d2f110b59160e1a1d281e2d0e0d17e2c1beb8f5d5d7e1eeddecced7c29dc0daed87d0d9b08d8e9188fa85b69f94a7bbbea4d98a9c81db93849d2f3240735479'),
    (88, 1, 182, '78614d6e48575469134b46174b43574853030b3315746607113d191d1557453e015c1a1f184eeec5b0f3e0c4a2d2d2eee9c69cced39ae0ecd2cf8fea8c8ba7a394e99b98e9a9b9a2d5859fbe83cd9ab6c6773731787f655c457a575a451411456054005e7f6a0c2f151d0d3c3e672202282a343e2506460014410d35eacee1e9fce6d0d4d0'),
    (75, 2, 16, 'qLSmsMjUqsbC0patz6C9nLii57fJxurW3rin167kxd3r3vfBs-S60Lrb9tfm0L7w0sXB79Di1fgE2fjDzAjq8w7OA9H0Dert9_Ie7x0A4g7i7gXb9BLq5uMuAQou6APqKB8GCik3-TwwNiY2LRcUIfg'),
    (92, 2, 212, 'qWKLeH1imqeNhp6zjY61o5GRsIWQeb63oo-grcCDsLShk5Sil7-sna_QxaG0n73Qo7XTzNu7z5fi05rMocfbuNfQut67v8nZ0e2r8bDq9Om31OT0-9fd9L3Y2NHF8u35-NL5-uPjC-7g7-Ls7A__BwUX8vfc3N8JIRUC5AMbGSfkJSge-OvmKi4mIwQBJg')
]
_0x98d7f07f9 = [
    (2, 1, 58, '0d0823267b722a306733686457025450550a1417414e48b4b6e1e9eea4aba3a0a5a996c19a999cd3d084dfdea5a1f7f0f9aeb6ece9e9ecd1d2'),
    (7, 0, 240, 'c4d6c8cad9d0df8c8a6e756b6e615a7568577a626a3e38382d2a33306e'),
    (3, 1, 181, '8a8f8df7a6a1aefae1e3e5e9bfeddadd8a88dcd3ced59e945f676766607673653a373c431043181c070455015d0820717b2f7d6262636a645202075b0f0e114248184da3bea5eee4cfe1f3fdfdf0ce8784899a89858e8285'),
    (6, 0, 23, '7c292a43171717131740151b1e1e124a4e184e54131e11444c425f5757654d594f4d562f2f607966'),
    (1, 2, 203, 'BAL68TxAMzc5RzU9QUdBQE5NUEhOVQQdBhg'),
    (0, 2, 6, 'gSlueHx4bYEwSTJiWGNXSDhDOoKNjpGCgn6BlURdVVxeWl9bX2M'),
    (4, 2, 201, 'MgP_MwoFNDgFOQo7EfwH_k0_WExQQ0dDWE5IGh4gDSYPHlMlKiIpVykqWQ'),
    (5, 1, 124, 'e3b4e6eeb5a7a2a5adf9afc492cc9a9c86d0848a8df5f6a4f0f8acb3eceebfbdd1d3')
]
__2585ji2n = "55b0bc3a170a7995ed3c908c844ae62f79c36a08cd0cc6530ee1e8ead1cb9e2e"
_O011IoI60e4 = "0d5906c44b70cd69ac49b55003d721d7f0e43178da0ba75c65472f23749fc6ad"
INTEGRITY_SCRIPT_SHA256 = "259b8bef6c8e4951ef957c335fe487eeebee97f6d53f0a111186a6e1ed783df6"
__p68dcb4 = None
_41d049976bd293 = {
    '0x4157d0257e45': (1251, 1, 61, '454f4f4f435c1d475d4f4d2029683d2c227c253c3036043a1b180b1d11040f22e5eee9faa3c7c5b8faecb3c4cdccc5c2e29cdbd6df91a7a0bca2a9fefbeda9ad94978e'),
    '_apkqhtyb0fdc': (652, 1, 165, '4557524e523213232d230c2b25'),
    '320138e51ee686': (917, 1, 221, '1c000a'),
    't_a0ccb1fe8': (3727, 1, 181, '74697b6222363e3a322a0309451f0d140018082de5e7e9caf5ff'),
    'g_864fcedb6c2': (2808, 1, 92, '2d252e3305'),
    'I1O0ll01a3ba': (1317, 2, 138, 'Dg8eExwiFBU'),
    '0x982a54': (3241, 0, 150, '6e061101706a'),
    '507b2280e1b04a': (2700, 1, 162, '1d7264716b'),
    '_w008e026': (1507, 0, 217, 'dad2ccd2a1b5'),
    '_i63qpmg7dru': (1892, 0, 218, '4e5e392d2d22201a352f297b7f7d'),
    '_7lxe7lav92gqvt': (2020, 2, 221, 'LTEkKCo4JjEt'),
    '_u83003cbf2c5': (1409, 1, 56, 'cdd2d6b0b5baaea9bfbdb185af8587878680'),
    '0x1e7aecc0c5': (2270, 2, 102, 'tKa_s7eqrqq1sQ'),
    'lo01b252': (2317, 1, 11, '6c7a41454152595e59'),
    '3bda804c66376b': (2632, 2, 236, 'pqqkq6Gmn5qvrJ2yqKJ0eHo')
}
_7d5161e5ed4461 = {}


def _l00ooe83c(__1diegy1gtj3):
    return hashlib.sha256(__1diegy1gtj3.encode("utf-8")).hexdigest()


def _0xcf4d7274ba5(__70aw2hh1, __tac212d26, _ll1llO7dd4, _loll0I1c13):
    if __tac212d26 == 0:
        _O011f3a9 = bytes.fromhex(_loll0I1c13)
        return bytes(
            __1diegy1gtj3 ^ ((_ll1llO7dd4 + __70aw2hh1 + _9cd3181b68ca4a) & 0xFF)
            for _9cd3181b68ca4a, __1diegy1gtj3 in enumerate(_O011f3a9)
        )
    if __tac212d26 == 1:
        _O011f3a9 = bytes.fromhex(_loll0I1c13)
        return bytes(
            __1diegy1gtj3 ^ ((_ll1llO7dd4 + __70aw2hh1 + _9cd3181b68ca4a * 3) & 0xFF)
            for _9cd3181b68ca4a, __1diegy1gtj3 in enumerate(_O011f3a9)
        )[::-1]
    _b269770789ff86 = "=" * ((4 - len(_loll0I1c13) % 4) % 4)
    _O011f3a9 = base64.urlsafe_b64decode(_loll0I1c13 + _b269770789ff86)
    return bytes(
        (__1diegy1gtj3 - _ll1llO7dd4 - __70aw2hh1 - _9cd3181b68ca4a) & 0xFF
        for _9cd3181b68ca4a, __1diegy1gtj3 in enumerate(_O011f3a9)
    )


def __d8tdydxdpu2(parts):
    _o0oI1110a389 = []
    for __70aw2hh1, __tac212d26, _ll1llO7dd4, _loll0I1c13 in sorted(parts):
        _o0oI1110a389.append(_0xcf4d7274ba5(__70aw2hh1, __tac212d26, _ll1llO7dd4, _loll0I1c13).decode("utf-8"))
    return "".join(_o0oI1110a389)


def _0xa729be(_0xac2ec49ee4fc7):
    _0x652d570d = _7d5161e5ed4461.get(_0xac2ec49ee4fc7)
    if _0x652d570d is not None:
        return _0x652d570d
    _0x9225f9fc6df9d = _41d049976bd293[_0xac2ec49ee4fc7]
    _0x652d570d = _0xcf4d7274ba5(*_0x9225f9fc6df9d).decode("utf-8")
    _7d5161e5ed4461[_0xac2ec49ee4fc7] = _0x652d570d
    return _0x652d570d


def __yf32282f74bc32(_f_0ab07af0):
    __jmlwlefu4m28w62 = {
        "format": "",
        "loader_id": "",
        "loader_fingerprint": "",
        "payload_id": "",
        "issued_at": 0,
    }
    if not isinstance(_f_0ab07af0, str) or not _f_0ab07af0.startswith("QFPC3."):
        return __jmlwlefu4m28w62

    try:
        _O011f3a9 = base64.urlsafe_b64decode(_f_0ab07af0[6:] + "=" * ((4 - len(_f_0ab07af0[6:]) % 4) % 4))
    except Exception:
        return __jmlwlefu4m28w62

    if len(_O011f3a9) < 18 or _O011f3a9[:4] != b"QFPC" or _O011f3a9[4] != 3:
        return __jmlwlefu4m28w62

    _4c613f670b5c72 = _O011f3a9[16]
    _ea721be137ffb1 = _O011f3a9[6]
    _f_b534f1 = _O011f3a9[7]
    __hr60zs5u8i = int.from_bytes(_O011f3a9[8:10], "big")
    _3f456241b5b679 = 18 + _4c613f670b5c72 + _ea721be137ffb1 + _f_b534f1
    _I1lIO0o1368 = _3f456241b5b679 + __hr60zs5u8i
    if _4c613f670b5c72 <= 0 or len(_O011f3a9) < _I1lIO0o1368:
        return __jmlwlefu4m28w62

    __oo675du2hjd44g = _O011f3a9[18:18 + _4c613f670b5c72]
    _z_dca8f32de3 = _O011f3a9[_3f456241b5b679:_I1lIO0o1368]
    __t9zdizjd5cb = b"|loader:" + __oo675du2hjd44g + b"|fp:"
    try:
        __cdd7pkz10e3f = _z_dca8f32de3.index(__t9zdizjd5cb) + len(__t9zdizjd5cb)
        _7536cef8d1d01e = _z_dca8f32de3[__cdd7pkz10e3f:__cdd7pkz10e3f + 32]
        _lO0llIlc4d6 = _z_dca8f32de3.index(b"|pid:", __cdd7pkz10e3f + 32) + len(b"|pid:")
        _976f8e7fdfc6aa = _z_dca8f32de3[_lO0llIlc4d6:_lO0llIlc4d6 + 16]
        _a_971d34 = _z_dca8f32de3.index(b"|iat:", _lO0llIlc4d6 + 16) + len(b"|iat:")
        _h_55efb67b55d = int.from_bytes(_z_dca8f32de3[_a_971d34:_a_971d34 + 8], "big")
    except ValueError:
        return __jmlwlefu4m28w62

    return {
        _0xa729be("_w008e026"): _0xa729be("507b2280e1b04a"),
        _0xa729be("_7lxe7lav92gqvt"): __oo675du2hjd44g.hex(),
        _0xa729be("_u83003cbf2c5"): _7536cef8d1d01e.hex(),
        _0xa729be("0x1e7aecc0c5"): _976f8e7fdfc6aa.hex(),
        _0xa729be("lo01b252"): _h_55efb67b55d,
    }


def _50e85fe77ec9e5(__p6e6sfkiwstguix):
    return "".join(
        __5cmtfv8z0 for __5cmtfv8z0 in __p6e6sfkiwstguix.splitlines(keepends=True)
        if not __5cmtfv8z0.startswith('INTEGRITY_SCRIPT_SHA256 = "')
    )


def _oooIIOO29cd():
    global __p68dcb4
    if __p68dcb4 is None:
        _e_8c2f5f160036d = __d8tdydxdpu2(_0x98d7f07f9)
        __p68dcb4 = json.loads(_e_8c2f5f160036d)
    return __p68dcb4


def _e_d222226f():
    if __y4262310546331 < 0:
        return ""
    return __d8tdydxdpu2(_e_785210dfe)


_l1I1Oofdb0 = _e_d222226f()


def _Oll01l0O2b49():
    _k_b03cc0943 = _l00ooe83c(_l1I1Oofdb0)
    if not hmac.compare_digest(_k_b03cc0943, _O011IoI60e4):
        print("完整性校验失败: 加密载荷已被篡改")
        return False
    return True


def _d_230e71a61e():
    global __p68dcb4
    _e_8c2f5f160036d = __d8tdydxdpu2(_0x98d7f07f9)
    _k_b03cc0943 = _l00ooe83c(_e_8c2f5f160036d)
    if not hmac.compare_digest(_k_b03cc0943, __2585ji2n):
        print("完整性校验失败: 运行清单已被篡改")
        return False

    try:
        _e0739960756d9b = __p68dcb4
        if _e0739960756d9b is None:
            _e0739960756d9b = json.loads(_e_8c2f5f160036d)
            __p68dcb4 = _e0739960756d9b
    except Exception:
        print("完整性校验失败: 运行清单格式无效")
        return False

    if _e0739960756d9b.get(_0xa729be("_w008e026")) != _0xa729be("507b2280e1b04a"):
        print("完整性校验失败: 运行清单版本无效")
        return False
    if _e0739960756d9b.get(_0xa729be("_i63qpmg7dru")) != _O011IoI60e4:
        print("完整性校验失败: 运行清单与载荷不匹配")
        return False
    if not _e0739960756d9b.get(_0xa729be("_7lxe7lav92gqvt")):
        print("完整性校验失败: 加密载荷缺少 loader 绑定信息")
        return False
    if not _e0739960756d9b.get(_0xa729be("_u83003cbf2c5")):
        print("完整性校验失败: 加密载荷缺少 loader 指纹")
        return False
    if not _e0739960756d9b.get(_0xa729be("0x1e7aecc0c5")):
        print("完整性校验失败: 加密载荷缺少 payload 标识")
        return False
    if not _e0739960756d9b.get(_0xa729be("lo01b252")):
        print("完整性校验失败: 加密载荷缺少签发时间")
        return False

    payload_metadata = __yf32282f74bc32(_l1I1Oofdb0)
    for _ll1llO7dd4 in (
        _0xa729be("_w008e026"),
        _0xa729be("_7lxe7lav92gqvt"),
        _0xa729be("_u83003cbf2c5"),
        _0xa729be("0x1e7aecc0c5"),
        _0xa729be("lo01b252"),
    ):
        if _e0739960756d9b.get(_ll1llO7dd4) != payload_metadata.get(_ll1llO7dd4):
            print("完整性校验失败: 运行清单与加密载荷不匹配")
            return False
    return True


def _IlI0o19d4(_9ff09c312cf114):
    __ajd2340yto = os.stat(_9ff09c312cf114)
    return (
        getattr(__ajd2340yto, "st_dev", None),
        getattr(__ajd2340yto, "st_ino", None),
        __ajd2340yto.st_size,
        getattr(__ajd2340yto, "st_mtime_ns", int(__ajd2340yto.st_mtime * 1000000000)),
    )


def _c_f825d0(__ubycpknpa):
    try:
        _e0739960756d9b = _oooIIOO29cd()
    except Exception:
        return False

    _0xe89a6a167b8 = _e0739960756d9b.get(_0xa729be("3bda804c66376b")) or ""
    if not _0xe89a6a167b8:
        return True

    _v_142de2be919 = hashlib.sha256()
    try:
        with open(__ubycpknpa, "rb") as _c8054f38aca503:
            for _w_2cc715 in iter(lambda: _c8054f38aca503.read(1024 * 1024), b""):
                _v_142de2be919.update(_w_2cc715)
    except Exception:
        print("完整性校验失败: 无法读取 pyCodeProtect.so")
        return False

    if not hmac.compare_digest(_v_142de2be919.hexdigest(), _0xe89a6a167b8):
        print("完整性校验失败: pyCodeProtect.so 与加密载荷不匹配")
        return False
    return True


def _h_36019465c(__ubycpknpa):
    __mqx68w1w1 = _0xa729be("_apkqhtyb0fdc")
    sys.modules.pop(__mqx68w1w1, None)

    loader = importlib.machinery.ExtensionFileLoader(__mqx68w1w1, __ubycpknpa)
    _q_4cfbdd83e = importlib.util.spec_from_file_location(__mqx68w1w1, __ubycpknpa, loader=loader)
    if _q_4cfbdd83e is None or _q_4cfbdd83e.loader is None:
        raise RuntimeError("无法加载 pyCodeProtect.so")

    _da498766aac08d = importlib.util.module_from_spec(_q_4cfbdd83e)
    try:
        sys.modules[__mqx68w1w1] = _da498766aac08d
        _q_4cfbdd83e.loader.exec_module(_da498766aac08d)
    except Exception:
        sys.modules.pop(__mqx68w1w1, None)
        raise

    _0xff581413 = os.path.realpath(getattr(_da498766aac08d, "__file__", ""))
    _44f739342bf6b6 = os.path.realpath(__ubycpknpa)
    if _0xff581413 != _44f739342bf6b6:
        raise RuntimeError("运行库加载路径不匹配")

    return _da498766aac08d


def __oxyno27az(_da498766aac08d):
    try:
        _e0739960756d9b = _oooIIOO29cd()
        _d33b8a03287911 = _da498766aac08d.info()
    except Exception:
        print("完整性校验失败: 无法读取运行库身份")
        return False

    if _d33b8a03287911.get(_0xa729be("_w008e026")) != _0xa729be("507b2280e1b04a"):
        print("完整性校验失败: 运行库格式不匹配")
        return False
    if _d33b8a03287911.get(_0xa729be("_7lxe7lav92gqvt")) != _e0739960756d9b.get(_0xa729be("_7lxe7lav92gqvt")):
        print("完整性校验失败: 运行库 loader_id 不匹配")
        return False
    if _d33b8a03287911.get(_0xa729be("_u83003cbf2c5")) != _e0739960756d9b.get(_0xa729be("_u83003cbf2c5")):
        print("完整性校验失败: 运行库 loader 指纹不匹配")
        return False
    return True


def _79ea774aafeb3d():
    __exchx49kao22 = os.path.abspath(__file__)
    try:
        with open(__exchx49kao22, "r", encoding="utf-8") as _0x051db5d795ad5:
            _i_b4312bd9a = _0x051db5d795ad5.read()
    except Exception as _01a0db08bfce01:
        print(f"完整性校验失败: 无法读取当前脚本: {_01a0db08bfce01}")
        return False

    __icedc6e91be681 = _50e85fe77ec9e5(_i_b4312bd9a)
    _k_b03cc0943 = _l00ooe83c(__icedc6e91be681)

    if not hmac.compare_digest(_k_b03cc0943, INTEGRITY_SCRIPT_SHA256):
        print("完整性校验失败: 启动器文件已被篡改")
        return False

    return True


def _0x5ab1da2d73():
    return _Oll01l0O2b49() and _d_230e71a61e() and _79ea774aafeb3d()


def _b8197c0acc55c0(_0xa43e4ab4):
    try:
        _da498766aac08d = __tolqbcjpck105jq
        getattr(_da498766aac08d, _0xa729be("320138e51ee686"))(_0xa43e4ab4)
    except Exception:
        print("执行出错: 运行库拒绝执行或载荷无效")


__mc980356 = _0xa729be("0x4157d0257e45")


def _0xa0a7d1b():
    _x_96c17648961 = sys.version_info
    __qcc536d5f93f = f"{_x_96c17648961.major}{_x_96c17648961.minor}"

    __qwuhda4mcyp8 = platform.machine().lower()
    if __qwuhda4mcyp8 in ("x86_64", "amd64"):
        __qclt951hz = "x86_64"
    elif __qwuhda4mcyp8 in ("aarch64", "arm64"):
        __qclt951hz = "aarch64"
    elif __qwuhda4mcyp8.startswith("armv7"):
        __qclt951hz = "armv7l"
    else:
        return ""

    return f"pyCodeProtect_{__qcc536d5f93f}_{__qclt951hz}.so"


def _oo11IO1cc41(__b070ip6a, _x_29f47d9a6):
    __yde01c768885 = []
    if _x_29f47d9a6:
        __yde01c768885.append(os.path.join(__b070ip6a, _x_29f47d9a6))
    __yde01c768885.append(os.path.join(__b070ip6a, "pyCodeProtect.so"))
    for _9ff09c312cf114 in __yde01c768885:
        if os.path.isfile(_9ff09c312cf114):
            return os.path.realpath(_9ff09c312cf114)
    return ""


def _0xe676c3(__b070ip6a, _x_29f47d9a6):
    if not _x_29f47d9a6:
        print("无法识别当前平台架构，跳过自动下载")
        return ""

    __kysqhknd7 = f"{__mc980356}/{_x_29f47d9a6}"
    __q2598c92fdbe = os.path.join(__b070ip6a, _x_29f47d9a6)

    print(f"未找到本地运行库，正在下载: {_x_29f47d9a6}")
    print(f"下载地址: {__kysqhknd7}")

    _0xca2db311a, __9oupfba0y7tgkr = tempfile.mkstemp(dir=__b070ip6a, suffix=".so.tmp")
    try:
        os.close(_0xca2db311a)
        __ht1aydux0edyyr = urllib.request.Request(__kysqhknd7, headers={"User-Agent": _0xa729be("t_a0ccb1fe8")})
        with urllib.request.urlopen(__ht1aydux0edyyr, timeout=60) as _0x0299e35b54ce, open(__9oupfba0y7tgkr, "wb") as _loOo0149f4:
            for _w_2cc715 in iter(lambda: _0x0299e35b54ce.read(1024 * 1024), b""):
                _loOo0149f4.write(_w_2cc715)
        if os.path.getsize(__9oupfba0y7tgkr) <= 0:
            print("下载失败: 运行库文件为空")
            return ""
        os.replace(__9oupfba0y7tgkr, __q2598c92fdbe)
        print(f"下载完成: {__q2598c92fdbe}")
        return os.path.realpath(__q2598c92fdbe)
    except urllib.error.HTTPError as _01a0db08bfce01:
        print(f"下载失败: HTTP {_01a0db08bfce01.code} — 可能暂不支持当前平台/Python 版本")
        return ""
    except urllib.error.URLError as _01a0db08bfce01:
        print(f"下载失败: 网络错误 — {_01a0db08bfce01.reason}")
        return ""
    except Exception as _01a0db08bfce01:
        print(f"下载失败: {_01a0db08bfce01}")
        return ""
    finally:
        try:
            if os.path.exists(__9oupfba0y7tgkr):
                os.unlink(__9oupfba0y7tgkr)
        except OSError:
            pass


def _6306a3b8de885d(__ubycpknpa, _x_29f47d9a6):
    return bool(_x_29f47d9a6) and os.path.basename(__ubycpknpa) == _x_29f47d9a6


def _I1OIoo1l96d3(__ubycpknpa, _x_29f47d9a6):
    if not _6306a3b8de885d(__ubycpknpa, _x_29f47d9a6):
        return
    try:
        os.remove(__ubycpknpa)
        print(f"已删除不匹配的运行库缓存: {__ubycpknpa}")
    except OSError:
        pass


__tolqbcjpck105jq = None


def _q_c7ee4b(__1diegy1gtj3):
    return ((__1diegy1gtj3 ^ 0x5A5A) - (__1diegy1gtj3 & 0)) == (__1diegy1gtj3 ^ 0x5A5A)


def _8972719548d44a():
    if not _q_c7ee4b(len(_e_785210dfe) + __y4262310546331):
        return
    if not _0x5ab1da2d73():
        return

    __b070ip6a = os.path.dirname(os.path.abspath(__file__))
    _x_29f47d9a6 = _0xa0a7d1b()

    __ubycpknpa = _oo11IO1cc41(__b070ip6a, _x_29f47d9a6)
    __l63be3f6172b59 = False

    if __ubycpknpa:
        print(f"本地发现运行库: {os.path.basename(__ubycpknpa)}")
    else:
        __ubycpknpa = _0xe676c3(__b070ip6a, _x_29f47d9a6)
        if not __ubycpknpa:
            print("无法获取运行库，请手动将对应平台的 pyCodeProtect.so 放至脚本同目录后重试")
            return
        __l63be3f6172b59 = True

    try:
        _k_c6989073 = _IlI0o19d4(__ubycpknpa)
    except OSError:
        print("完整性校验失败: 无法读取 pyCodeProtect.so 文件状态")
        return

    __wc360795cfb940 = _6306a3b8de885d(__ubycpknpa, _x_29f47d9a6)

    if not __wc360795cfb940:
        if not _c_f825d0(__ubycpknpa):
            return
    else:
        if __l63be3f6172b59:
            print("注意: 跨平台下载模式，已跳过文件 hash 校验，仅校验模块身份")
        else:
            print("注意: 检测到架构命名运行库，已跳过文件 hash 校验，仅校验模块身份")

    global __tolqbcjpck105jq
    try:
        __tolqbcjpck105jq = _h_36019465c(__ubycpknpa)
        _o_db45be456823 = _IlI0o19d4(__ubycpknpa)
    except Exception:
        print("执行出错: 无法安全加载 pyCodeProtect.so")
        return

    if _k_c6989073 != _o_db45be456823:
        print("完整性校验失败: pyCodeProtect.so 在加载期间发生变化")
        return

    if not __oxyno27az(__tolqbcjpck105jq):
        _I1OIoo1l96d3(__ubycpknpa, _x_29f47d9a6)
        return

    _b8197c0acc55c0(_l1I1Oofdb0)


_o01l10O63d7 = {_0xa729be("g_864fcedb6c2"): _8972719548d44a}


if __name__ == _0xa729be("I1O0ll01a3ba"):
    __l6357bf82c = _0xa729be("g_864fcedb6c2")
    _o01l10O63d7.get(__l6357bf82c, lambda: None)()
