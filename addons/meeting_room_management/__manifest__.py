{
    'name': 'Quản lý Phòng họp & Hội trường',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Management',
    'summary': 'Quản lý phòng họp, đăng ký mượn phòng, lịch sử mượn phòng',
    'depends': ['base', 'mail'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/phong_hop_views.xml',
        'views/dang_ky_muon_phong_views.xml',
        'views/lich_su_muon_phong_views.xml',
        'views/thong_ke_su_dung_phong_views.xml',
        'views/thiet_bi_views.xml',
        'views/lich_su_bao_tri_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}
