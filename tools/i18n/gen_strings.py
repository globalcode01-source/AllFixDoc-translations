"""
Uygulama metinlerinin tek kaynağı. İngilizce (varsayılan) ve Türkçe bu dosyada; diğer diller translations/<dil>.py
içinde (T sözlüğü ve PRIVACY metni). Çalıştırma:

    python3 tools/i18n/gen_strings.py app/src/main/res

Her çeviride yer tutucular (%1$s, %1$d, %%) İngilizceyle aynı olmalı; değilse üretim durur. Eksik anahtarlar
İngilizceye düşer ve sayısı yazdırılır.
"""
import sys

# Diğer betikler (review_export.py) yalnızca metin tablolarını okumak için içe aktarabilsin
RES = sys.argv[1] if __name__ == "__main__" else None

# key: (english, turkish)
S = {
    # Common actions
    "action_ok": ("OK", "Tamam"),
    "action_cancel": ("Cancel", "İptal"),
    "action_close": ("Close", "Kapat"),
    "action_save": ("Save", "Kaydet"),
    "action_delete": ("Delete", "Sil"),
    "action_copy": ("Copy", "Kopyala"),
    "action_share": ("Share", "Paylaş"),
    "action_open": ("Open", "Aç"),
    "action_change": ("Change", "Değiştir"),

    # Bottom navigation and files
    "nav_home": ("Home", "Ana sayfa"),
    "nav_files": ("Files", "Dosyalar"),
    "files_favorites": ("Favorites", "Favoriler"),
    "files_folders": ("Folders", "Klasörler"),
    "files_favorite": ("Favorite", "Favori"),
    "files_add_favorite": ("Add to favorites", "Favorilere ekle"),
    "files_unfavorite": ("Remove from favorites", "Favorilerden çıkar"),
    "files_favorites_empty": (
        "No favorites yet. Use the menu next to a file to add it.",
        "Henüz favori yok. Eklemek için dosyanın yanındaki menüyü kullan.",
    ),
    "files_add_folder": ("Add folder", "Klasör ekle"),
    "files_remove_folder": ("Remove folder", "Klasörü kaldır"),
    "files_folders_empty": (
        "Add a folder to see all the PDFs in it. Only the folders you choose are read — no storage permission needed.",
        "İçindeki tüm PDF'leri görmek için bir klasör ekle. Yalnızca seçtiğin klasörler okunur; depolama izni gerekmez.",
    ),
    "tools_search": ("Search tools", "Araç ara"),
    "tools_search_clear": ("Clear search", "Aramayı temizle"),
    "tools_no_results": ("No matching tools", "Eşleşen araç yok"),
    "tools_cat_all": ("All", "Tümü"),
    "tools_cat_edit": ("Edit & organize", "Düzenle"),
    "tools_cat_convert": ("Convert & export", "Dönüştür ve dışa aktar"),
    "tools_cat_security": ("Security", "Güvenlik"),
    "tools_cat_scan": ("Scan & smart", "Tara ve akıllı"),
    "tool_compress": ("Compress PDF", "PDF sıkıştır"),
    "tool_compress_desc": ("Make the file smaller by shrinking images", "Görselleri küçülterek dosya boyutunu azalt"),
    "tool_compress_action": ("Compress", "Sıkıştır"),
    "tool_compress_done": ("PDF compressed", "PDF sıkıştırıldı"),
    "tool_compress_suffix": ("compressed", "sikistirilmis"),
    "tool_compress_low": ("Light", "Hafif"),
    "tool_compress_low_desc": ("Best quality, smaller savings", "En iyi kalite, daha az kazanç"),
    "tool_compress_medium": ("Recommended", "Önerilen"),
    "tool_compress_medium_desc": ("Good quality, clearly smaller file", "İyi kalite, belirgin küçülme"),
    "tool_compress_high": ("Strong", "Güçlü"),
    "tool_compress_high_desc": ("Smallest file, images lose detail", "En küçük dosya, görseller ayrıntı kaybeder"),
    "tool_compress_note": ("Text stays sharp; only photos and scanned images are shrunk. The original file is not changed.", "Yazılar keskin kalır; yalnızca fotoğraflar ve taranmış görseller küçültülür. Asıl dosya değişmez."),
    "tool_pdf_to_image": ("PDF to image", "PDF'ten görsele"),
    "tool_pdf_to_image_desc": ("Save pages as JPG or PNG, or as one long image", "Sayfaları JPG/PNG ya da tek uzun görsel olarak kaydet"),
    "tool_pdf_to_image_done": ("Images saved", "Görseller kaydedildi"),
    "tool_pdf_to_image_gallery_done": ("Images saved to Pictures › AllFixDoc", "Görseller Resimler › AllFixDoc klasörüne kaydedildi"),
    "tool_image_all_pages": ("All pages", "Tüm sayfalar"),
    "tool_image_range": ("Page range", "Sayfa aralığı"),
    "tool_image_format": ("Format", "Biçim"),
    "tool_image_quality": ("Quality", "Kalite"),
    "tool_image_q_screen": ("Screen", "Ekran"),
    "tool_image_q_normal": ("Standard", "Standart"),
    "tool_image_q_print": ("Print", "Baskı"),
    "tool_image_long": ("One long image", "Tek uzun görsel"),
    "tool_image_long_desc": ("Pages are joined top to bottom; handy for sharing in chats", "Sayfalar alt alta birleşir; sohbette paylaşmak için pratik"),
    "tool_image_action": ("Save", "Kaydet"),
    "tool_print": ("Print", "Yazdır"),
    "tool_print_desc": ("Print or save with a printer service", "Yazıcıya gönder ya da yazdırma hizmetiyle kaydet"),
    "error_print_restricted": ("The owner of this document doesn't allow printing.", "Belgenin sahibi yazdırmaya izin vermiyor."),
    "tool_apply": ("Apply", "Uygula"),
    "tool_watermark": ("Watermark", "Filigran"),
    "tool_watermark_desc": ("Stamp text such as CONFIDENTIAL on every page", "Her sayfaya GİZLİ gibi bir yazı bas"),
    "tool_watermark_done": ("Watermark added", "Filigran eklendi"),
    "tool_watermark_suffix": ("watermarked", "filigranli"),
    "tool_watermark_default": ("CONFIDENTIAL", "GİZLİ"),
    "tool_watermark_text": ("Text", "Metin"),
    "tool_watermark_color": ("Color", "Renk"),
    "tool_watermark_opacity": ("Opacity: %1$d%%", "Saydamlık: %%%1$d"),
    "tool_watermark_diagonal": ("Diagonal", "Çapraz"),
    "tool_page_numbers": ("Page numbers", "Sayfa numarası"),
    "tool_page_numbers_desc": ("Number the pages at the top or bottom", "Sayfaları altta ya da üstte numaralandır"),
    "tool_page_numbers_done": ("Page numbers added", "Sayfa numaraları eklendi"),
    "tool_page_numbers_suffix": ("numbered", "numarali"),
    "tool_page_numbers_word": ("Page", "Sayfa"),
    "tool_page_numbers_position": ("Position", "Konum"),
    "tool_page_numbers_skip_first": ("Don't number the first page (cover)", "İlk sayfayı (kapak) numaralandırma"),
    "tool_pos_bottom_center": ("Bottom center", "Alt orta"),
    "tool_pos_bottom_right": ("Bottom right", "Alt sağ"),
    "tool_pos_bottom_left": ("Bottom left", "Alt sol"),
    "tool_pos_top_right": ("Top right", "Üst sağ"),
    "tool_qr_create": ("Create QR code", "QR kod oluştur"),
    "tool_qr_create_desc": ("Turn a link or text into a QR code", "Bağlantı ya da metni QR koda çevir"),
    "tool_qr_create_done": ("QR code saved", "QR kod kaydedildi"),
    "tool_qr_create_hint": ("Link or text", "Bağlantı ya da metin"),
    "tool_qr_create_empty": ("Type something to see the QR code", "QR kodu görmek için bir şey yaz"),
    "export_text": ("Export as text", "Metin olarak dışa aktar"),
    "export_text_done": ("Text saved", "Metin kaydedildi"),
    "export_text_page": ("Page %1$d", "Sayfa %1$d"),
    "ai_quick_translate_tr": ("Translate to Turkish", "Türkçeye çevir"),
    "ai_prompt_translate_tr": ("Translate the document into Turkish.", "Belgeyi Türkçeye çevir."),
    "ai_quick_translate_en": ("Translate to English", "İngilizceye çevir"),
    "ai_prompt_translate_en": ("Translate the document into English.", "Belgeyi İngilizceye çevir."),
    "ai_quick_rewrite": ("Rewrite", "Yeniden yaz"),
    "ai_prompt_rewrite": ("Rewrite the document in clearer, simpler sentences without changing its meaning.", "Belgeyi anlamını değiştirmeden daha açık ve sade cümlelerle yeniden yaz."),
    "pro_tool_body": ("This tool is part of Pro. A one-time purchase unlocks it and removes ads; everything else stays free.", "Bu araç Pro sürümde. Tek seferlik satın alma ile açılır ve reklamlar da kalkar; diğer her şey ücretsiz kalır."),
    "pro_tool_buy_price": ("Get Pro · %1$s", "Pro al · %1$s"),
    "default_section": ("Default app", "Varsayılan uygulama"),
    "default_title": ("App for opening PDFs", "PDF'leri açan uygulama"),
    "default_status_us": ("AllFixDoc (set)", "AllFixDoc (ayarlı)"),
    "default_status_none": ("Not set; Android asks every time", "Seçilmedi; Android her seferinde soruyor"),
    "default_status_other": ("Currently: %1$s", "Şu an: %1$s"),
    "default_is_us": ("PDFs already open in AllFixDoc.", "PDF'ler zaten AllFixDoc ile açılıyor."),
    "default_other": ("PDFs currently open in %1$s.", "PDF'ler şu an %1$s ile açılıyor."),
    "default_other_steps": ("Android doesn't let apps change this themselves. In %1$s's settings, open “Open by default” and clear the defaults. The next time you open a PDF, choose AllFixDoc and “Always”.", "Android bunu uygulamaların kendisinin değiştirmesine izin vermiyor. %1$s ayarlarında “Varsayılan olarak aç” bölümüne girip varsayılanları temizle. Sonra bir PDF açarken AllFixDoc'u ve “Her zaman”ı seç."),
    "default_none_steps": ("Open a PDF from your Files app or a download, choose AllFixDoc and tap “Always”.", "Dosyalar uygulamasından ya da indirilenlerden bir PDF aç, AllFixDoc'u seç ve “Her zaman”a dokun."),
    "default_open_settings": ("Open %1$s settings", "%1$s ayarlarını aç"),
    "default_hint_title": ("Open PDFs with AllFixDoc", "PDF'leri AllFixDoc ile aç"),
    "default_hint_body": ("Make it the default so PDFs from mail and downloads open here.", "Varsayılan yap; e-postadan ve indirilenlerden gelen PDF'ler burada açılsın."),
    "default_hint_action": ("Show how", "Nasıl yapılır"),
    "feedback_title": ("Send feedback", "Geri bildirim gönder"),
    "feedback_desc": ("Report a problem or suggest a feature", "Sorun bildir ya da özellik öner"),
    "feedback_subject": ("AllFixDoc feedback", "AllFixDoc geri bildirim"),
    "rate_title": ("Rate the app", "Uygulamayı değerlendir"),
    "rate_desc": ("Leave a review on Google Play", "Google Play'de yorum yap"),
    "tools_cat_files": ("Files & images", "Dosya ve görsel"),
    "tool_zip_create": ("Create ZIP", "ZIP oluştur"),
    "tool_zip_create_desc": ("Pack several files into one ZIP", "Birden fazla dosyayı tek ZIP'te topla"),
    "tool_zip_create_done": ("ZIP created", "ZIP oluşturuldu"),
    "tool_zip_file": ("files", "dosyalar"),
    "tool_zip_extract": ("Extract ZIP", "ZIP aç"),
    "tool_zip_extract_desc": ("Extract the files in a ZIP archive", "ZIP arşivindeki dosyaları çıkar"),
    "tool_zip_extract_done": ("Files extracted", "Dosyalar çıkarıldı"),
    "tool_zip_extract_done_downloads": ("Extracted to Downloads › AllFixDoc", "İndirilenler › AllFixDoc klasörüne çıkarıldı"),
    "tool_zip_count": ("%1$d files", "%1$d dosya"),
    "tool_zip_empty": ("The archive is empty.", "Arşiv boş."),
    "tool_zip_invalid": ("This ZIP can't be opened. It may be damaged or password-protected.", "Bu ZIP açılamadı. Bozuk ya da şifreli olabilir."),
    "tool_zip_too_large": ("The archive is too large to extract on the phone.", "Arşiv telefonda açılamayacak kadar büyük."),
    "tool_img_title": ("Processing images", "Görseller işleniyor"),
    "tool_img_compress": ("Compress images", "Görsel sıkıştır"),
    "tool_img_compress_desc": ("Make photos smaller for sharing", "Fotoğrafları paylaşmak için küçült"),
    "tool_img_resize": ("Resize images", "Görsel boyutlandır"),
    "tool_img_resize_desc": ("Change the pixel size of photos", "Fotoğrafların piksel boyutunu değiştir"),
    "tool_img_convert": ("Convert images", "Görsel dönüştür"),
    "tool_img_convert_desc": ("Convert between JPG, PNG and WEBP", "JPG, PNG ve WEBP arasında dönüştür"),
    "tool_img_size": ("Longest side", "En uzun kenar"),
    "tool_img_size_original": ("Original", "Orijinal"),
    "tool_img_quality": ("Quality: %1$d", "Kalite: %1$d"),
    "tool_img_note": ("Originals aren't changed. Location and camera details are removed from the copies.", "Asıl görseller değişmez. Kopyalardan konum ve kamera bilgileri silinir."),
    "tool_img_count": ("%1$d images", "%1$d görsel"),
    "tool_img_folder": ("Images", "Gorseller"),
    "tool_img_done": ("Images saved", "Görseller kaydedildi"),
    "tool_img_done_gallery": ("Saved to Pictures › AllFixDoc", "Resimler › AllFixDoc klasörüne kaydedildi"),
    "tool_gif_create": ("Images to GIF", "Görsellerden GIF"),
    "tool_gif_create_desc": ("Turn photos into an animated GIF", "Fotoğrafları hareketli GIF'e çevir"),
    "tool_gif_create_done": ("GIF created", "GIF oluşturuldu"),
    "tool_gif_speed": ("Time per frame", "Kare süresi"),
    "tool_gif_seconds": ("%1$.1f s", "%1$.1f sn"),
    "tool_gif_frames": ("GIF to frames", "GIF'i karelere ayır"),
    "tool_gif_frames_desc": ("Save each frame of a GIF as an image", "GIF'in her karesini görsel olarak kaydet"),
    "tool_gif_frames_done": ("Frames saved", "Kareler kaydedildi"),
    "tool_gif_frames_done_gallery": ("Frames saved to Pictures › AllFixDoc", "Kareler Resimler › AllFixDoc klasörüne kaydedildi"),
    "tool_gif_frame_count": ("%1$d frames", "%1$d kare"),
    "tool_gif_invalid": ("This GIF can't be read.", "Bu GIF okunamadı."),
    "files_hint_title": ("See all your PDFs here", "Tüm PDF'lerin burada görünsün"),
    "files_hint_body": ("Add your Documents folder (or any other) and its PDFs are listed automatically. No storage permission needed.", "Belgeler klasörünü (ya da başka bir klasörü) ekle; içindeki PDF'ler otomatik listelensin. Depolama izni gerekmez."),
    "files_hint_action": ("Add Documents", "Belgeler'i ekle"),
    "office_converting": ("Opening the document…", "Belge açılıyor…"),
    "office_unsupported": ("This file can't be opened. It may be password-protected, damaged, or in a format without a public specification (for example old SoftMaker .tmd or Microsoft Works). Save it as DOCX, ODT or PDF and try again.", "Bu dosya açılamadı. Şifreli, bozuk ya da belgesi yayımlanmamış bir biçimde olabilir (örneğin eski SoftMaker .tmd ya da Microsoft Works). DOCX, ODT ya da PDF olarak kaydedip yeniden dene."),
    "office_failed": ("The document couldn't be converted.", "Belge dönüştürülemedi."),
    "tool_office_pdf": ("Office to PDF", "Office'ten PDF"),
    "tool_office_pdf_desc": ("Word, Excel, PowerPoint, LibreOffice, WPS, RTF, CSV or image (JPG, TIFF) to PDF", "Word, Excel, PowerPoint, LibreOffice, WPS, RTF, CSV ya da görseli (JPG, TIFF) PDF'e çevir"),
    "tool_office_pdf_done": ("PDF created", "PDF oluşturuldu"),
    "tool_pdf_word": ("PDF to Word", "PDF'ten Word'e"),
    "tool_pdf_word_desc": ("Get the text as an editable Word file", "Metni düzenlenebilir Word dosyası olarak al"),
    "tool_pdf_word_done": ("Word file created", "Word dosyası oluşturuldu"),
    "tool_pdf_excel": ("PDF to Excel", "PDF'ten Excel'e"),
    "tool_pdf_excel_desc": ("Turn tables in a PDF into a spreadsheet", "PDF'teki tabloları Excel tablosuna çevir"),
    "tool_pdf_excel_done": ("Excel file created", "Excel dosyası oluşturuldu"),
    "tool_pdf_office_no_text": ("This PDF has no text. If it's scanned, run text recognition (OCR) in the viewer first and save it as searchable.", "Bu PDF'te metin yok. Taranmışsa önce görüntüleyicide metin tanımayı (OCR) çalıştırıp aranabilir olarak kaydet."),
    "settings_pro_tools": ("Pro tools: %1$s. Everything else stays free.", "Pro araçları: %1$s. Diğer her şey ücretsiz."),
    "appearance_title": ("Appearance", "Görünüm"),
    "appearance_mode": ("Theme", "Tema"),
    "appearance_mode_system": ("System", "Sistem"),
    "appearance_mode_light": ("Light", "Açık"),
    "appearance_mode_dark": ("Dark", "Koyu"),
    "appearance_color": ("Color", "Renk"),
    "appearance_color_auto": ("Wallpaper colors", "Duvar kâğıdı renkleri"),
    "appearance_color_blue": ("Blue", "Mavi"),
    "appearance_color_green": ("Green", "Yeşil"),
    "appearance_color_teal": ("Teal", "Turkuaz"),
    "appearance_color_purple": ("Purple", "Mor"),
    "appearance_color_burgundy": ("Burgundy & blue", "Bordo-mavi"),
    "appearance_color_orange": ("Orange", "Turuncu"),
    "appearance_color_red": ("Red", "Kırmızı"),
    "appearance_black": ("Pure black dark theme", "Saf siyah koyu tema"),
    "appearance_black_desc": ("Black background in dark theme; saves battery on OLED screens", "Koyu temada arka plan siyah olur; OLED ekranlarda pil tasarrufu sağlar"),
    "icon_style": ("Icon style", "Simge stili"),
    "icon_style_filled": ("Filled", "Dolgulu"),
    "icon_style_outlined": ("Outlined", "Çizgili"),
    "icon_style_rounded": ("Rounded", "Yuvarlak"),
    "icon_style_two_tone": ("Two-tone", "İki tonlu"),
    "appearance_icon": ("App icon", "Uygulama simgesi"),
    "icon_default": ("AllFixDoc", "AllFixDoc"),
    "icon_dark": ("Night", "Gece"),
    "icon_sunset": ("Sunset", "Gün batımı"),
    "icon_forest": ("Forest", "Orman"),
    "icon_changed": ("Icon changed. It may take a few seconds to update; if the home screen shortcut disappears, add it again from the app list.", "Simge değiştirildi. Güncellenmesi birkaç saniye sürebilir; ana ekrandaki kısayol kaybolursa uygulama listesinden yeniden ekle."),
    "arc_menu_open": ("Open quick menu", "Hızlı menüyü aç"),
    "arc_menu_setting": ("Half-circle quick menu", "Yarım daire hızlı menü"),
    "arc_menu_setting_desc": ("A handle on the left edge opens a rotating menu of your tools; swipe up or down to turn it", "Sol kenardaki tutamak araçlarının olduğu dönen menüyü açar; çevirmek için yukarı-aşağı kaydır"),
    "link_open_title": ("Open this link?", "Bu bağlantı açılsın mı?"),
    "office_preview_only": ("Apple iWork file: only the preview saved inside the file is shown. For the full document, export it as PDF from Pages, Numbers or Keynote.", "Apple iWork dosyası: yalnızca dosyanın içindeki önizleme gösteriliyor. Belgenin tamamı için Pages, Numbers ya da Keynote'tan PDF olarak dışa aktar."),
    "tool_redact": ("Redact", "Karart"),
    "tool_redact_hint": ("Drag over what you want to hide. When you save, the page becomes an image and the hidden text is permanently removed from the file.", "Gizlemek istediğin yeri sürükleyerek işaretle. Kaydedince sayfa görüntüye çevrilir ve gizlenen metin dosyadan kalıcı olarak silinir."),
    "redact_added_hint": ("Marked for redaction. Text on this page will no longer be selectable after saving; save as a copy to keep the original.", "Karartma eklendi. Kaydettikten sonra bu sayfadaki metin seçilemez olur; aslını korumak için kopya olarak kaydet."),
    "settings_language": ("Language", "Dil"),
    "language_system": ("Phone language (%1$s)", "Telefonun dili (%1$s)"),
    "just_now": ("Just now", "Az önce"),
    "files_no_pdfs": ("No PDFs in these folders.", "Bu klasörlerde PDF yok."),
    # Home
    "home_open_pdf": ("Open document", "Belge aç"),
    "home_recent": ("Recent", "Son açılanlar"),
    "home_empty_title": ("No documents yet", "Henüz belge yok"),
    "home_empty_body": (
        "Open a PDF or Office document from your device. AllFixDoc only reads the files you choose — no storage permission needed.",
        "Cihazından bir PDF ya da Office belgesi aç. AllFixDoc yalnızca senin seçtiğin dosyaları okur; depolama izni istemez.",
    ),
    "home_remove_from_list": ("Remove from list", "Listeden kaldır"),
    "home_clear_list": ("Clear list", "Listeyi temizle"),
    "home_page_progress": ("Page %1$d of %2$d", "Sayfa %1$d / %2$d"),
    "home_more": ("More", "Diğer"),

    # Viewer
    "viewer_back": ("Back", "Geri"),
    "viewer_go_to_page": ("Go to page", "Sayfaya git"),
    "viewer_page_number": ("Page number (1–%1$d)", "Sayfa numarası (1–%1$d)"),
    "viewer_go": ("Go", "Git"),
    "viewer_night_mode": ("Night mode", "Gece modu"),
    "viewer_share": ("Share", "Paylaş"),
    "viewer_info": ("Document info", "Belge bilgisi"),
    "viewer_page_indicator": ("%1$d / %2$d", "%1$d / %2$d"),
    "viewer_error": ("This file couldn't be opened. It may be damaged or not a PDF.", "Dosya açılamadı. Bozuk olabilir ya da PDF değil."),
    "viewer_password_title": ("Password protected", "Şifreli belge"),
    "viewer_password_body": ("This document is locked. Enter its password to open it.", "Bu belge kilitli. Açmak için şifresini gir."),
    "viewer_password_wrong": ("Wrong password. Try again.", "Şifre yanlış. Tekrar dene."),
    "viewer_password_hint": ("Password", "Şifre"),
    "viewer_unlock": ("Unlock", "Kilidi aç"),
    "viewer_info_title": ("Title", "Başlık"),
    "viewer_info_author": ("Author", "Yazar"),
    "viewer_info_pages": ("Pages", "Sayfa sayısı"),
    "viewer_info_producer": ("Created with", "Oluşturan"),
    "viewer_info_file": ("File", "Dosya"),
    "viewer_share_chooser": ("Share PDF", "PDF'i paylaş"),
    "password_repeat": ("Repeat password", "Şifreyi tekrarla"),

    # Viewer menu
    "menu_search": ("Search", "Ara"),
    "menu_bookmark": ("Bookmark this page", "Bu sayfaya yer imi koy"),
    "menu_edit": ("Edit and annotate", "Düzenle ve not al"),
    "menu_navigate": ("Contents and pages", "İçindekiler ve sayfalar"),
    "menu_present": ("Present (projector)", "Sunum yap (projektör)"),
    "present_projector_hint": ("To show slides on a projector, connect a cable (HDMI/USB-C) or turn on Screen cast / Smart View on your phone. Slides go to the projector, notes stay on your phone.", "Slaytları projektörde göstermek için kablo (HDMI/USB-C) bağla ya da telefonun Ekran yansıtma / Smart View özelliğini aç. Slaytlar projektöre gider, notlar telefonda kalır."),
    "present_projector": ("Projector: %1$s", "Projektör: %1$s"),
    "present_up_next": ("Up next", "Sıradaki"),
    "present_end": ("End of presentation", "Sunumun sonu"),
    "present_notes": ("Speaker notes", "Konuşmacı notları"),
    "present_no_notes": ("No notes for this slide. Tap to add one.", "Bu slaytta not yok. Eklemek için dokun."),
    "present_note_title": ("Note for slide %1$d", "%1$d. slaytın notu"),
    "present_blanked": ("The audience sees a blank screen", "Seyirci boş ekran görüyor"),
    "present_timer_reset": ("Reset timer", "Sayacı sıfırla"),
    "present_previous": ("Previous slide", "Önceki slayt"),
    "present_next": ("Next slide", "Sonraki slayt"),
    "present_laser": ("Laser pointer", "Lazer işaretçi"),
    "present_pen": ("Pen", "Kalem"),
    "present_clear": ("Clear drawing", "Çizimi sil"),
    "present_black": ("Black screen", "Siyah ekran"),
    "present_white": ("White screen", "Beyaz ekran"),
    "present_exit": ("End presentation", "Sunumu bitir"),
    "present_play_video": ("Play video", "Videoyu oynat"),
    "present_play_audio": ("Play sound", "Sesi oynat"),
    "video_error": ("This video can't be played on this device.", "Bu video bu cihazda oynatılamıyor."),
    "video_rewind": ("Back 10 seconds", "10 saniye geri"),
    "video_forward": ("Forward 10 seconds", "10 saniye ileri"),
    "video_close": ("Close video", "Videoyu kapat"),
    "video_on_projector": ("Playing on the projector: %1$s", "Projektörde oynatılıyor: %1$s"),
    "video_projector_hint": ("To play on a projector, connect a cable (HDMI/USB-C) or turn on Screen cast / Smart View. The video goes to the projector, the controls stay on your phone.", "Projektörde oynatmak için kablo (HDMI/USB-C) bağla ya da Ekran yansıtma / Smart View'u aç. Video projektöre gider, denetimler telefonda kalır."),
    "tool_video_project": ("Play video on projector", "Videoyu projektörde oynat"),
    "tool_video_project_desc": ("Video on the projector or TV, controls on your phone", "Video projektörde ya da TV'de, denetimler telefonda"),
    "viewer_read_only": ("UYAP (UDF) documents can't be edited. You can read, share, print and save them as PDF.", "UYAP (UDF) belgeleri düzenlenemez. Okuyabilir, paylaşabilir, yazdırabilir ve PDF olarak kaydedebilirsin."),
    "viewer_read_only_label": ("Read-only", "Yalnızca okunur"),
    "home_present": ("Present", "Sunum"),
    "consent_title": ("Data transfer abroad", "Yurt dışına veri aktarımı"),
    "consent_body_startup": ("To show ads in the free version and keep the app's settings up to date, AllFixDoc sends your IP address and advertising ID to Google (AdMob) and GitHub servers in the USA. This transfer abroad needs your explicit consent (KVKK art. 9). If you don't agree, no ads are shown and every feature still works.", "Ücretsiz sürümde reklam göstermek ve uygulama ayarlarını güncel tutmak için AllFixDoc, IP adresini ve reklam kimliğini ABD'deki Google (AdMob) ve GitHub sunucularına gönderir. Bu yurt dışı aktarım için açık rızan gerekir (KVKK m.9). Kabul etmezsen reklam gösterilmez, tüm özellikler yine çalışır."),
    "consent_body_ai": ("The text of the pages you choose and your questions are sent, with your key, to the servers of the AI service you selected, which are abroad. This needs your explicit consent (KVKK art. 9).", "Seçtiğin sayfaların metni ve soruların, senin anahtarınla seçtiğin AI servisinin yurt dışındaki sunucularına gönderilir. Bunun için açık rızan gerekir (KVKK m.9)."),
    "consent_body_mlkit": ("Scanning, text recognition, QR codes and interface translation use Google ML Kit. Images and text are processed on your device, but Google Play services downloads the needed modules and may send diagnostic data to Google servers abroad. This needs your explicit consent (KVKK art. 9).", "Belge tarama, metin tanıma, QR kodları ve arayüz çevirisi Google ML Kit'i kullanır. Görüntüler ve metin cihazında işlenir; ancak Google Play hizmetleri gerekli modülleri indirir ve yurt dışındaki Google sunucularına tanılama verisi gönderebilir. Bunun için açık rızan gerekir (KVKK m.9)."),
    "consent_body_speech": ("Voice input uses your device's speech recognition service (usually Google); your voice may be processed on its servers abroad. AllFixDoc doesn't record or keep audio. This needs your explicit consent (KVKK art. 9).", "Sesle yazma, cihazının konuşma tanıma servisini (çoğunlukla Google) kullanır; sesin yurt dışındaki sunucularında işlenebilir. AllFixDoc ses kaydetmez, saklamaz. Bunun için açık rızan gerekir (KVKK m.9)."),
    "consent_change_later": ("You can change this any time in Settings › Privacy.", "Bunu istediğin zaman Ayarlar › Gizlilik'ten değiştirebilirsin."),
    "consent_accept": ("I agree", "Kabul ediyorum"),
    "consent_reject": ("I don't agree", "Kabul etmiyorum"),
    "consent_read_notice": ("Read the privacy notice", "Aydınlatma metnini oku"),
    "consent_denied": ("This feature needs your consent to the transfer abroad. You can turn it on in Settings › Privacy.", "Bu özellik yurt dışı aktarım iznin olmadan çalışmaz. Ayarlar › Gizlilik'ten açabilirsin."),
    "consent_settings_title": ("Transfers abroad", "Yurt dışına aktarım izinleri"),
    "consent_label_startup": ("Ads and app settings (Google, GitHub)", "Reklam ve uygulama ayarı (Google, GitHub)"),
    "consent_label_ai": ("AI assistant (the service you choose)", "AI asistanı (seçtiğin servis)"),
    "consent_label_mlkit": ("Scan, text recognition, QR and translation (Google ML Kit)", "Tarama, metin tanıma, QR ve çeviri (Google ML Kit)"),
    "consent_label_speech": ("Voice input (device speech service)", "Sesle yazma (cihazın konuşma servisi)"),
    "consent_switch_desc": ("When off, no data is sent; the feature asks again when you use it.", "Kapalıyken veri gönderilmez; özelliği kullanınca yeniden sorulur."),
    "menu_read_aloud": ("Read aloud", "Sesli oku"),
    "menu_ai": ("AI assistant", "AI asistan"),
    "menu_ocr": ("Recognize text (OCR)", "Metni tanı (OCR)"),
    "menu_form": ("Fill in form", "Formu doldur"),
    "menu_codes": ("Read QR and barcodes on this page", "Bu sayfadaki QR ve barkodları oku"),
    "menu_searchable": ("Save as searchable PDF", "Aranabilir PDF olarak kaydet"),

    # Search
    "search_hint": ("Search in document", "Belgede ara"),
    "search_count": ("%1$d/%2$d", "%1$d/%2$d"),
    "search_none": ("No results", "Sonuç yok"),
    "search_next": ("Next result", "Sonraki sonuç"),
    "search_previous": ("Previous result", "Önceki sonuç"),

    # Navigation sheet
    "nav_contents": ("Contents", "İçindekiler"),
    "nav_bookmarks": ("Bookmarks", "Yer imleri"),
    "nav_pages": ("Pages", "Sayfalar"),
    "nav_page": ("Page %1$d", "Sayfa %1$d"),
    "nav_contents_empty": ("This document has no table of contents.", "Bu belgede içindekiler bölümü yok."),
    "nav_bookmarks_empty": (
        "No bookmarks yet. Tap the bookmark icon at the top to mark a page.",
        "Henüz yer imi yok. Bir sayfayı işaretlemek için üstteki yer imi simgesine dokun.",
    ),
    "bookmark_added": ("Bookmark added", "Yer imi eklendi"),
    "bookmark_removed": ("Bookmark removed", "Yer imi kaldırıldı"),

    # Selection
    "selection_replace": ("Replace text", "Metni değiştir"),
    "replace_warning": (
        "The new text is written over the old one. The original text may stay in the file, so don't use this to hide confidential information.",
        "Yeni metin eskisinin üzerine yazılır. Asıl metin dosyada kalabilir; gizli bilgiyi saklamak için kullanma.",
    ),

    # Editing
    "edit_title": ("Editing", "Düzenleme"),
    "edit_undo": ("Undo", "Geri al"),
    "edit_redo": ("Redo", "Yinele"),
    "edit_unsaved_hint": ("Change added. Save to keep it in the file.", "Değişiklik eklendi. Dosyada kalması için kaydet."),
    "tool_highlight": ("Highlight", "Vurgula"),
    "tool_ink": ("Draw", "Çiz"),
    "tool_note": ("Note", "Not"),
    "tool_text": ("Text", "Metin"),
    "tool_signature": ("Sign", "İmza"),
    "tool_eraser": ("Eraser", "Silgi"),
    "tool_highlight_hint": ("Drag over text to highlight it. Use two fingers to scroll.", "Vurgulamak için metnin üzerinde sürükle. Kaydırmak için iki parmak kullan."),
    "tool_ink_hint": ("Draw with one finger. Use two fingers to scroll and zoom.", "Tek parmakla çiz. Kaydırmak ve yakınlaştırmak için iki parmak kullan."),
    "tool_note_hint": ("Tap where you want to add a note.", "Not eklemek istediğin yere dokun."),
    "voice_input": ("Speak to type", "Sesle yaz"),
    "voice_input_unavailable": ("Speech input isn't available on this device.", "Bu cihazda sesle yazma kullanılamıyor."),
    "tool_text_hint": ("Tap to add text. Tap added text to change it.", "Metin eklemek için dokun. Eklenen metne dokunarak değiştir."),
    "tool_edit_text": ("Edit text", "Metni düzenle"),
    "tool_edit_text_hint": ("Tap a line to edit it right there. Tap an empty spot to write new text.", "Bir satıra dokun, olduğu yerde düzenle. Boş bir yere dokunursan yeni metin yazarsın."),
    "tool_signature_hint": ("Tap where the signature should go.", "İmzanın gideceği yere dokun."),
    "tool_eraser_hint": ("Tap an unsaved change to remove it.", "Kaydedilmemiş bir değişikliği silmek için üzerine dokun."),
    "note_add_title": ("Add note", "Not ekle"),
    "text_add_title": ("Add text", "Metin ekle"),
    "text_edit_title": ("Edit text", "Metni düzenle"),

    # Signatures
    "signature_pick_title": ("Choose signature", "İmza seç"),
    "signature_new": ("New signature", "Yeni imza"),
    "signature_delete": ("Delete signature", "İmzayı sil"),
    "signature_draw_title": ("Draw your signature", "İmzanı çiz"),
    "signature_draw_hint": (
        "Signatures are stored only on this device and are not included in backups.",
        "İmzalar yalnızca bu cihazda saklanır, yedeklemeye dahil edilmez.",
    ),
    "signature_clear": ("Clear", "Temizle"),
    "signature_choose": ("Choose signature", "İmza seç"),
    "signature_change": ("Change signature", "İmzayı değiştir"),

    # Saving
    "save_title": ("Save changes", "Değişiklikleri kaydet"),
    "save_body": (
        "Save into the original file, or keep the original and save a copy?",
        "Asıl dosyanın üzerine mi kaydedilsin, yoksa asıl dosya korunup bir kopya mı kaydedilsin?",
    ),
    "save_body_copy_only": (
        "This file can't be changed directly (for example, it was opened from another app). Save the result as a copy.",
        "Bu dosya doğrudan değiştirilemiyor (örneğin başka bir uygulamadan açıldı). Sonucu kopya olarak kaydet.",
    ),
    "save_overwrite": ("Save", "Üzerine kaydet"),
    "save_copy": ("Save a copy", "Kopya olarak kaydet"),
    "save_as_pdf": ("Save as PDF", "PDF olarak kaydet"),
    "save_copy_suffix": ("edited", "duzenlendi"),
    "save_progress": ("Saving…", "Kaydediliyor…"),
    "save_done": ("Saved", "Kaydedildi"),
    "save_failed": ("Couldn't save: %1$s", "Kaydedilemedi: %1$s"),
    "tool_interrupted": ("The operation was interrupted while choosing where to save. Please try again.", "Kaydetme yeri seçilirken işlem yarıda kaldı. Lütfen tekrar dene."),
    "error_restricted": ("The owner of this document doesn't allow this change.", "Belgenin sahibi bu değişikliğe izin vermiyor."),
    "unsaved_title": ("Unsaved changes", "Kaydedilmemiş değişiklikler"),
    "unsaved_body": ("Your notes and edits haven't been saved to the file yet.", "Notların ve düzenlemelerin henüz dosyaya kaydedilmedi."),
    "unsaved_discard": ("Discard", "Kaydetme"),

    # Forms
    "form_title": ("Fill in form", "Formu doldur"),
    "form_empty": ("This document has no fillable fields.", "Bu belgede doldurulabilir alan yok."),

    # OCR
    "ocr_title": ("Recognize text", "Metni tanı"),
    "ocr_body": (
        "Text recognition (OCR) turns scanned pages into searchable, selectable text that can also be read aloud and used by the AI assistant. It runs on your device.",
        "Metin tanıma (OCR), taranmış sayfaları aranabilir ve seçilebilir metne çevirir; bu metin sesli okunabilir ve AI asistanı tarafından kullanılabilir. İşlem cihazında yapılır.",
    ),
    "ocr_all": ("Whole document", "Tüm belge"),
    "ocr_this_page": ("This page", "Bu sayfa"),
    "ocr_progress": ("Recognizing text… %1$d/%2$d", "Metin tanınıyor… %1$d/%2$d"),
    "ocr_not_needed": ("These pages already contain text; OCR isn't needed.", "Bu sayfalarda zaten metin var; OCR gerekmiyor."),
    "ocr_done": ("Text recognized on %1$s page(s)", "%1$s sayfada metin tanındı"),
    "ocr_failed": ("Text recognition failed: %1$s", "Metin tanıma başarısız: %1$s"),

    # QR
    "qr_title": ("QR codes and barcodes", "QR kodları ve barkodlar"),
    "qr_none": ("No codes found.", "Kod bulunamadı."),
    "qr_open": ("Open", "Aç"),
    "qr_scanning": ("Looking for codes…", "Kodlar aranıyor…"),

    # Read aloud
    "tts_title": ("Reading aloud", "Sesli okuma"),
    "tts_no_text": ("No text to read. Run text recognition (OCR) first.", "Okunacak metin yok. Önce metni tanı (OCR)."),
    "tts_voice_error": (
        "The voice for this language isn't installed.",
        "Bu dilin sesi yüklü değil.",
    ),
    "tts_voice_settings": ("Voice settings", "Ses ayarları"),
    "tts_play": ("Play", "Oynat"),
    "tts_pause": ("Pause", "Duraklat"),
    "tts_next": ("Next page", "Sonraki sayfa"),
    "tts_previous": ("Previous page", "Önceki sayfa"),

    # AI
    "ai_title": ("AI assistant", "AI asistan"),
    "ai_scope_all": ("Whole document", "Tüm belge"),
    "ai_scope_page": ("Page %1$d", "Sayfa %1$d"),
    "ai_input_hint": ("Ask about this document", "Belge hakkında soru sor"),
    "ai_send": ("Send", "Gönder"),
    "ai_stop": ("Stop", "Durdur"),
    "ai_thinking": ("Thinking…", "Düşünüyor…"),
    "ai_usage": ("Tokens: %1$d in (%2$d from cache) · %3$d out", "Token: %1$d girdi (%2$d önbellekten) · %3$d çıktı"),
    "ai_privacy_note": ('The text of the selected pages and your questions are sent to the AI service you chose, using your own API key.', 'Seçilen sayfaların metni ve soruların, senin API anahtarınla seçtiğin AI servisine gönderilir.'),
    "ai_quick_summary": ("Summarize", "Özetle"),
    "ai_quick_points": ("Key points", "Ana noktalar"),
    "ai_quick_simple": ("Explain simply", "Basitçe anlat"),
    "ai_prompt_summary": (
        "Summarize this document in a few short paragraphs. Mention the most important pages.",
        "Bu belgeyi birkaç kısa paragrafta özetle. En önemli sayfaları belirt.",
    ),
    "ai_prompt_points": (
        "List the key points of this document as short bullet points, each with its page number.",
        "Bu belgenin ana noktalarını, her birinin sayfa numarasıyla birlikte kısa maddeler hâlinde listele.",
    ),
    "ai_prompt_simple": (
        "Explain what this document says in simple language, as if to someone without background in the subject.",
        "Bu belgenin ne anlattığını, konuya yabancı birine anlatır gibi basit bir dille açıkla.",
    ),
    "ai_no_text": (
        "No text was found in these pages. If the document is scanned, run text recognition (OCR) first.",
        "Bu sayfalarda metin bulunamadı. Belge taranmışsa önce metni tanı (OCR).",
    ),
    "ai_key_title": ("Anthropic API key", "Anthropic API anahtarı"),
    "ai_key_label": ("API key", "API anahtarı"),
    "ai_key_body": (
        "Create a key in the Anthropic Console. It is stored encrypted on this device and used only for your AI requests. Usage is billed to your Anthropic account.",
        "Anahtarı Anthropic Console'da oluştur. Bu cihazda şifreli saklanır ve yalnızca senin AI isteklerin için kullanılır. Kullanım ücreti Anthropic hesabına yansır.",
    ),
    "ai_key_add": ("Add key", "Anahtar ekle"),
    "ai_key_missing_title": ("Add your API key", "API anahtarını ekle"),
    "ai_key_missing_body": (
        "The AI assistant summarizes documents and answers questions about them. It uses your own Anthropic API key, so you stay in control of usage and cost.",
        "AI asistanı belgeleri özetler ve onlarla ilgili soruları yanıtlar. Kendi Anthropic API anahtarını kullanır; kullanım ve maliyet senin kontrolündedir.",
    ),
    "ai_large_title": ("Long document", "Uzun belge"),
    "ai_large_body": ('The selected text is about %1$d thousand tokens. Sending it may use a large part of your AI service quota or cost more. Continue?', 'Seçilen metin yaklaşık %1$d bin token. Göndermek AI servisindeki kotanın büyük kısmını kullanabilir ya da ek ücrete yol açabilir. Devam edilsin mi?'),
    "ai_model_opus": ("Claude Opus 5.5 — most capable (default)", "Claude Opus 5.5 — en yetenekli (varsayılan)"),
    "ai_model_sonnet": ("Claude Sonnet 5.5 — faster, lower cost", "Claude Sonnet 5.5 — daha hızlı, daha düşük maliyet"),
    "ai_model_haiku": ("Claude Haiku 5.5 — fastest, lowest cost", "Claude Haiku 5.5 — en hızlı, en düşük maliyet"),
    "ai_error_no_key": ('Add an API key for the selected AI service in Settings to use the AI assistant.', "AI asistanını kullanmak için Ayarlar'dan seçili AI servisinin API anahtarını ekle."),
    "ai_error_refusal": ("The AI declined to answer this request. Try rephrasing your question.", "AI bu isteği yanıtlamadı. Sorunu farklı şekilde sormayı dene."),
    "ai_error_too_long": ("The selected text is too long for the AI. Choose fewer pages.", "Seçilen metin AI için çok uzun. Daha az sayfa seç."),
    "ai_truncated": ("(The answer was cut off because it reached the length limit.)", "(Yanıt uzunluk sınırına ulaştığı için kesildi.)"),
    "ai_error_key": ("The API key was rejected. Check it in Settings.", "API anahtarı reddedildi. Ayarlar'dan kontrol et."),
    "ai_error_permission": ("This API key isn't allowed to use the selected model.", "Bu API anahtarının seçili modeli kullanma izni yok."),
    "ai_error_rate": ("Too many requests. Wait a moment and try again.", "Çok fazla istek gönderildi. Biraz bekleyip tekrar dene."),
    "ai_error_request": ("The request was rejected: %1$s", "İstek reddedildi: %1$s"),
    "ai_error_service": ("The AI service returned an error (%1$d). Try again later.", "AI servisi hata döndürdü (%1$d). Daha sonra tekrar dene."),
    "ai_error_local_network": ("Android 17 and later don't let apps reach servers on your home network (for example a local AI on 192.168.x.x). Use an internet address (https://…) for this service.", "Android 17 ve sonrası, uygulamaların ev ağındaki sunuculara (ör. 192.168.x.x'teki yerel yapay zekâ) bağlanmasına izin vermiyor. Bu servis için internet adresi (https://…) kullan."),
    "ai_error_network": ("Couldn't reach the AI service. Check your internet connection.", "AI servisine ulaşılamadı. İnternet bağlantını kontrol et."),

    # Tools
    "tools_title": ("Tools", "Araçlar"),
    "tools_all": ("All tools", "Tüm araçlar"),
    "tool_merge": ("Merge PDFs", "PDF birleştir"),
    "tool_merge_desc": ("Combine several PDFs into one file", "Birden fazla PDF'i tek dosyada topla"),
    "tool_merge_action": ("Merge", "Birleştir"),
    "tool_merge_done": ("PDFs merged", "PDF'ler birleştirildi"),
    "tool_merge_file": ("merged", "birlesik"),
    "tool_merge_min": ("Add at least two files.", "En az iki dosya ekle."),
    "tool_split": ("Split PDF", "PDF böl"),
    "tool_split_desc": ("Extract a page range or split into parts", "Sayfa aralığı çıkar ya da parçalara ayır"),
    "tool_split_action": ("Split", "Böl"),
    "tool_split_done": ("Pages extracted", "Sayfalar çıkarıldı"),
    "tool_split_many_done": ("Parts saved to the selected folder", "Parçalar seçilen klasöre kaydedildi"),
    "tool_split_pages": ("The document has %1$d pages.", "Belgede %1$d sayfa var."),
    "tool_split_range": ("Extract pages", "Sayfa aralığını çıkar"),
    "tool_split_from": ("From", "Başlangıç"),
    "tool_split_to": ("To", "Bitiş"),
    "tool_split_every": ("Split into parts", "Parçalara böl"),
    "tool_split_every_label": ("Pages per part", "Parça başına sayfa"),
    "tool_organize": ("Organize pages", "Sayfaları düzenle"),
    "tool_organize_desc": ("Rotate, delete and reorder pages", "Sayfaları döndür, sil, sırala"),
    "organize_suffix": ("organized", "duzenli"),
    "organize_select_all": ("Select all", "Tümünü seç"),
    "organize_rotate_left": ("Rotate left", "Sola döndür"),
    "organize_rotate_right": ("Rotate right", "Sağa döndür"),
    "organize_move_up": ("Move earlier", "Öne al"),
    "organize_move_down": ("Move later", "Arkaya al"),
    "tool_scan": ("Scan document", "Belge tara"),
    "tool_scan_desc": ("Use the camera to create a clean PDF", "Kamerayla temiz bir PDF oluştur"),
    "tool_scan_done": ("Scan saved", "Tarama kaydedildi"),
    "tool_scan_fallback": (
        "Google's scanner couldn't open, so your phone camera is used instead.",
        "Google tarayıcısı açılamadı; telefonun kamerası kullanılıyor.",
    ),
    "tool_scan_file": ("scan", "tarama"),
    "tool_scan_unavailable": (
        "The document scanner isn't available on this device (Google Play services required).",
        "Belge tarayıcı bu cihazda kullanılamıyor (Google Play hizmetleri gerekli).",
    ),
    "tool_qr_unavailable": (
        "The QR scanner couldn't start. Check your internet connection and Google Play services, then try again.",
        "QR tarayıcı açılamadı. İnternet bağlantını ve Google Play hizmetlerini kontrol edip tekrar dene.",
    ),
    "tool_images": ("Images to PDF", "Görsellerden PDF"),
    "tool_images_desc": ("Turn photos into a PDF", "Fotoğrafları PDF'e çevir"),
    "tool_images_action": ("Create PDF", "PDF oluştur"),
    "tool_images_done": ("PDF created", "PDF oluşturuldu"),
    "tool_images_file": ("images", "gorseller"),
    "tool_images_a4": ("A4 pages", "A4 sayfa"),
    "tool_images_original": ("Original image size", "Görselin kendi boyutu"),
    "tool_add_more": ("Add more", "Daha fazla ekle"),
    "tool_protect": ("Add password", "Şifre ekle"),
    "tool_protect_desc": ("Lock a PDF with a password", "PDF'i şifreyle kilitle"),
    "tool_protect_body": (
        "Anyone opening the new copy will need this password. If you forget it, the file can't be opened.",
        "Yeni kopyayı açan herkes bu şifreye ihtiyaç duyar. Şifreyi unutursan dosya açılamaz.",
    ),
    "tool_protect_action": ("Lock", "Kilitle"),
    "tool_protect_done": ("Password-protected copy saved", "Şifreli kopya kaydedildi"),
    "tool_protected_suffix": ("locked", "sifreli"),
    "tool_unprotect": ("Remove password", "Şifreyi kaldır"),
    "tool_unprotect_desc": ("Save an unlocked copy", "Kilitsiz bir kopya kaydet"),
    "tool_unprotect_body": ("Enter the document's password to save a copy without it.", "Şifresiz bir kopya kaydetmek için belgenin şifresini gir."),
    "tool_unprotect_action": ("Remove", "Kaldır"),
    "tool_unprotect_done": ("Unlocked copy saved", "Kilitsiz kopya kaydedildi"),
    "tool_unlocked_suffix": ("unlocked", "kilitsiz"),
    "tool_qr": ("Scan QR code", "QR kod tara"),
    "tool_qr_desc": ("Read a QR code or barcode with the camera", "Kamerayla QR kod ya da barkod oku"),
    "tool_encrypted": ("This PDF is password protected. Remove its password first.", "Bu PDF şifreli. Önce şifresini kaldır."),
    "tool_failed": ("The operation failed.", "İşlem başarısız oldu."),

    # Settings
    "settings_title": ("Settings", "Ayarlar"),
    "settings_reading": ("Reading", "Okuma"),
    "settings_night_desc": ("Show pages with inverted colors", "Sayfaları ters renklerle göster"),
    "settings_screen_on": ("Keep screen on", "Ekranı açık tut"),
    "settings_screen_on_desc": ("While a document is open", "Belge açıkken"),
    "settings_tts_rate": ("Reading speed: %1$.2fx", "Okuma hızı: %1$.2fx"),
    "settings_tts_engine": ("Text-to-speech settings", "Metin okuma ayarları"),
    "settings_tts_engine_desc": ("Choose a voice or install one for your language", "Ses seç ya da Türkçe sesi yükle"),
    "ai_provider_claude_desc": ('Built-in; uses your Anthropic API key', 'Yerleşik; Anthropic API anahtarını kullanır'),
    "ai_assistant_add": ('Add assistant', 'Asistan ekle'),
    "ai_assistant_add_desc": ('Gemini, Groq, OpenRouter, Mistral or any OpenAI-compatible service — several have free tiers', 'Gemini, Groq, OpenRouter, Mistral ya da OpenAI uyumlu herhangi bir servis — birçoğunun ücretsiz katmanı var'),
    "ai_assistant_remove": ('Remove assistant?', 'Asistan kaldırılsın mı?'),
    "ai_assistant_custom": ('Custom', 'Özel'),
    "ai_assistant_free": ('free', 'ücretsiz'),
    "ai_assistant_get_key": ('Get a free %1$s key', 'Ücretsiz %1$s anahtarı al'),
    "ai_assistant_name": ('Name', 'Ad'),
    "ai_assistant_url": ('API address', 'API adresi'),
    "ai_assistant_url_hint": ('Must start with https://', 'https:// ile başlamalı'),
    "ai_assistant_model": ('Model', 'Model'),
    "ai_assistant_privacy": ('The document text you send is processed by this service under its own terms. The key is stored encrypted on this device only.', 'Gönderdiğin belge metni bu servis tarafından kendi koşullarıyla işlenir. Anahtar yalnızca bu cihazda şifreli saklanır.'),
    "tool_voice_notes": ('Voice notes', 'Sesli notlar'),
    "tool_voice_notes_desc": ('Speak to write notes; save as Word or TXT, or email them', 'Konuşarak not yaz; Word veya TXT olarak kaydet ya da e-postayla gönder'),
    "action_email": ('Email', 'E-posta ile gönder'),
    "ai_gemini_desc": ('Free key from Google AI Studio', "Google AI Studio'dan ücretsiz anahtar"),
    "ai_gemini_key_title": ('Google Gemini API key', 'Google Gemini API anahtarı'),
    "ai_gemini_key_body": ('Get a free key at aistudio.google.com and paste it here. It is stored encrypted on this device only.', 'aistudio.google.com adresinden ücretsiz anahtar alıp buraya yapıştır. Yalnızca bu cihazda şifreli saklanır.'),
    "ai_gemini_missing_body": ('Google Gemini is free to use with your own free API key from Google AI Studio.', "Google Gemini, Google AI Studio'dan alacağın ücretsiz anahtarla ücretsiz kullanılır."),
    "ai_other_assistants": ('Other assistants (optional)', 'Diğer asistanlar (isteğe bağlı)'),
    "voice_note_default_title": ('Note %1$s', 'Not %1$s'),
    "voice_speak_now": ('Speak now', 'Şimdi konuş'),
    "voice_note_hint": ('Tap the microphone and speak; each dictation is added as a new line. You can edit the text.', 'Mikrofona dokunup konuş; her söylediğin yeni satır olarak eklenir. Metni düzenleyebilirsin.'),
    "voice_note_title": ('Title', 'Başlık'),
    "voice_note_text": ('Note', 'Not'),
    "voice_note_saved": ('Saved', 'Kaydedildi'),
    "voice_note_save_failed": ("Couldn't save the file", 'Dosya kaydedilemedi'),
    "action_print": ('Print', 'Yazdır'),
    "print_failed": ("Couldn't prepare the file for printing", 'Dosya yazdırmaya hazırlanamadı'),
    "voice_note_history": ('My notes', 'Notlarım'),
    "voice_note_new": ('New note', 'Yeni not'),
    "voice_note_history_empty": ('No saved notes yet', 'Henüz kayıtlı not yok'),
    "voice_note_save_as": ('Save as', 'Farklı kaydet'),
    "voice_note_delete_confirm": ('Delete this note?', 'Bu not silinsin mi?'),
    "lang_auto_title": ('Automatic translation', 'Otomatik çeviri'),
    "lang_auto_desc": ("%1$s isn't built in. Translate the app on your device (Google ML Kit, about 30 MB over Wi‑Fi). Nothing is sent online; machine translation may contain mistakes.", "%1$s uygulamada hazır değil. Uygulamayı cihazında çevir (Google ML Kit, Wi‑Fi'de yaklaşık 30 MB). Hiçbir metin dışarı gönderilmez; makine çevirisi hata içerebilir."),
    "lang_auto_wifi": ('Waiting for Wi‑Fi to download the translation model (about 30 MB)', 'Çeviri modelini indirmek için Wi‑Fi bekleniyor (yaklaşık 30 MB)'),
    "lang_auto_working": ('Translating the app on your device…', 'Uygulama cihazında çevriliyor…'),
    "lang_auto_ready": ('On; translated on your device. Machine translation may contain mistakes.', 'Açık; cihazında çevrildi. Makine çevirisi hata içerebilir.'),
    "lang_auto_failed": ("Couldn't prepare the translation. It will retry next time the app opens.", 'Çeviri hazırlanamadı. Uygulama bir sonraki açılışta yeniden dener.'),
    "home_favorites": ('My favorites', 'Favorilerim'),
    "home_favorites_hint": ('Add with ☆ in Tools', "Araçlar'da ☆ ile ekle"),
    "home_locations": ('Locations', 'Konumlar'),
    "home_device": ('This device', 'Bu cihaz'),
    "home_other_clouds": ('Other Cloud', 'Diğer Bulut'),
    "cloud_title": ('Cloud storage', 'Bulut depolama'),
    "cloud_hint": ('Installed cloud apps appear in the file picker: open from there or save there.', 'Yüklü bulut uygulamaları dosya seçicide görünür: oradan aç ya da oraya kaydet.'),
    "cloud_open": ('Open', 'Aç'),
    "cloud_install": ('Install', 'Yükle'),
    "cloud_web": ('Website', 'Web sitesi'),
    "cloud_icloud_note": ('No Android app: download from icloud.com, then open from This device', "Android uygulaması yok: icloud.com'dan indir, sonra Bu cihaz'dan aç"),
    "home_tagline": ('PDF · Office · Scan · Notes · UYAP · Present · OCR', 'PDF · Office · Tarama · Notlar · UYAP · Sunum · OCR'),
    "settings_guide": ('User guide', 'Kullanım kılavuzu'),
    "settings_guide_desc": ('Features, tips and frequently asked questions', 'Özellikler, ipuçları ve sık sorulanlar'),
    "lang_auto_module": ('Downloading the translation component from Google Play…', "Çeviri bileşeni Google Play'den indiriliyor…"),
    "lang_auto_restart": ('Ready. Close and reopen the app to see it translated.', 'Hazır. Çevrilmiş hâlini görmek için uygulamayı kapatıp yeniden aç.'),
    "lang_auto_confirm": ('Download', 'İndir'),
    "lang_auto_confirm_desc": ('Google Play asks for your confirmation to download the translation component.', 'Google Play, çeviri bileşenini indirmek için onayını istiyor.'),
    "settings_ai": ("AI assistant", "AI asistan"),
    "settings_ai_key_saved": ("Saved on this device (encrypted)", "Bu cihazda kayıtlı (şifreli)"),
    "settings_ai_key_missing": ("Not added", "Eklenmedi"),
    "settings_ai_desc": (
        "Model used for summaries and questions. Faster models cost less; the most capable model gives the best answers.",
        "Özet ve sorular için kullanılan model. Hızlı modeller daha ucuzdur; en yetenekli model en iyi yanıtları verir.",
    ),
    "settings_pro": ("AllFixDoc Pro", "AllFixDoc Pro"),
    "settings_pro_active": ("Pro is active — no ads", "Pro etkin — reklam yok"),
    "settings_pro_buy": ("Remove ads", "Reklamları kaldır"),
    "settings_pro_buy_short": ("Buy", "Satın al"),
    "settings_pro_desc_ads": ("One-time purchase: removes ads. Every tool stays free.", "Tek seferlik satın alma: reklamları kaldırır. Bütün araçlar ücretsiz kalır."),
    "settings_pro_desc": ("One-time purchase: removes ads and unlocks the Pro tools.", "Tek seferlik satın alma: reklamları kaldırır ve Pro araçlarını açar."),
    "settings_pro_restore": ("Restore purchase", "Satın almayı geri yükle"),
    "settings_pro_unavailable": ("Google Play purchases aren't available right now.", "Google Play satın alma şu anda kullanılamıyor."),
    "settings_donate": ("Support us", "Bizi destekle"),
    "settings_donate_desc": (
        "One-time donation. It doesn't unlock features, but it helps us keep improving the app.",
        "Tek seferlik bağış. Özellik açmaz, ama uygulamanın gelişmesine yardım eder.",
    ),
    "settings_donate_thanks": ("Thank you for your support!", "Desteğin için teşekkürler!"),
    "settings_project_page": ("Project page", "Proje sayfası"),
    "settings_project_page_desc": (
        "Discover features, the guide and what's new on our project page, open to everyone on GitHub.",
        "Özellikleri, kılavuzu ve yenilikleri GitHub'da herkese açık proje sayfamızda keşfet.",
    ),
    "settings_privacy": ("Privacy", "Gizlilik"),
    "settings_ad_privacy": ("Ad privacy choices", "Reklam gizlilik tercihleri"),
    "settings_data": ("Data", "Veriler"),
    "backup_export": ("Export backup", "Yedeği dışa aktar"),
    "backup_export_desc": ("Settings, bookmarks and reading positions", "Ayarlar, yer imleri ve okuma konumları"),
    "backup_import": ("Import backup", "Yedeği içe aktar"),
    "backup_auto_desc": (
        "If Android backup is on, settings and bookmarks are also backed up to your Google account and restored on a new device.",
        "Android yedeklemesi açıksa ayarlar ve yer imleri Google hesabına da yedeklenir ve yeni cihazda geri yüklenir.",
    ),
    "backup_exported": ("Backup exported", "Yedek dışa aktarıldı"),
    "backup_imported": ("Backup imported", "Yedek içe aktarıldı"),
    "backup_failed": ("Couldn't export the backup", "Yedek dışa aktarılamadı"),
    "backup_invalid": ("This isn't an AllFixDoc backup file", "Bu bir AllFixDoc yedek dosyası değil"),
    "settings_clear_cache": ("Clear cache", "Önbelleği temizle"),
    "settings_clear_cache_desc": ("Preview images and OCR results", "Önizleme görselleri ve OCR sonuçları"),
    "settings_clear_cache_confirm": (
        "Preview images and recognized text (OCR) will be deleted from this device. Your documents are not affected.",
        "Önizleme görselleri ve tanınan metinler (OCR) bu cihazdan silinecek. Belgelerin etkilenmez.",
    ),
    "settings_cache_cleared": ("Cache cleared", "Önbellek temizlendi"),
    "settings_about": ("About", "Hakkında"),
    "settings_version": ("Version", "Sürüm"),
    "settings_support": ("Support", "Destek"),

    # Licenses and privacy
    "licenses_title": ("Open-source licenses", "Açık kaynak lisansları"),
    "licenses_intro": (
        "AllFixDoc is built with the following open-source components. Tap one to read its license.",
        "AllFixDoc aşağıdaki açık kaynak bileşenlerle geliştirildi. Lisansını okumak için birine dokun.",
    ),
    "licenses_website": ("Website", "Web sitesi"),
    "privacy_title": ("Privacy policy", "Gizlilik politikası"),
}

PRIVACY_EN = """AllFixDoc Privacy Policy
Last updated: 8 November 2026

AllFixDoc is a PDF reader and editor. This policy explains what data the app handles and why.

1. Your documents
AllFixDoc opens only the files you choose, through the Android file picker or "Open with". It doesn't request storage permission and doesn't scan your device. Documents are processed on your device and aren't uploaded by the app, except as described in section 4 when you use the AI assistant.

2. Data stored on your device
The app keeps the list of recently opened files and small preview images, bookmarks and reading positions, text recognized with OCR, signatures you draw, app settings and, if you add one, the API key of the AI service you chose, encrypted with a key held in your device's secure hardware. You can remove this data in Settings or by clearing the app's storage. In presentation mode it also keeps the speaker notes you write and the videos and sounds taken from presentations you open; these are not backed up.

3. Backups
If Android backup is on, Android may back up your settings, bookmarks and reading positions to your Google account. Your API key, signatures, OCR results, preview images and the recent files list are excluded. You can also export and import a backup file yourself.

4. AI assistant (optional)
The AI assistant works only after you add an API key for the service you choose: Google Gemini (default), Anthropic Claude, Groq, Mistral, OpenRouter or another service you add yourself. When you ask a question or request a summary, the text of the pages you selected and your messages are sent over an encrypted connection to that service only, using your key. The service processes this data under its own terms and privacy policy (for example policies.google.com, anthropic.com/legal). Keys are stored encrypted on your device. The developer of AllFixDoc doesn't receive this data. Dictating notes uses your device's speech recognition service (for example Google); AllFixDoc doesn't record or keep audio.

5. Text recognition, code reading and scanning
OCR, QR and barcode reading and document scanning use Google ML Kit through Google Play services. Images are processed on your device. Google Play services may collect diagnostic and usage information about these features under Google's privacy policy. If your phone's language isn't built into the app, the automatic translation downloads a Google ML Kit translation model once (over Wi‑Fi) and translates the interface on your device; no text leaves the device.

6. Advertising (free version)
The free version shows banner ads at the bottom of the Home, Files and Tools screens through Google AdMob, and occasionally a full-screen ad after a tool finishes its work. No ads are shown while you read or edit documents. In the European Economic Area and the UK you're asked for consent first, and you can change your choice in Settings. AdMob may collect device identifiers such as the advertising ID, approximate location derived from your IP address and ad interaction data to show and measure ads. See policies.google.com/technologies/ads.

7. Purchases
If you buy the ad-free Pro version, payment is handled by Google Play. The app only receives whether the purchase is active.

8. Children
AllFixDoc is not directed at children under 13.

9. Changes
When this policy changes, this page and the date above will be updated.

10. Contact
For questions about this policy, use the developer contact address on the app's Google Play page.

11. GDPR and KVKK
Data controller: Global Code 01 (globalcode01@gmail.com). The developer doesn't collect your documents or personal data; only if you write to us are your e-mail address and message used to reply. When the app starts it downloads a small settings file from the developer's site (globalcode01-source.github.io, on GitHub); only your IP address is sent. Google (AdMob, ML Kit, Play), GitHub and the AI service you choose (Google, Anthropic, Groq, Mistral, OpenRouter, etc.) run servers outside your country; when you use these features your IP address, and for the AI assistant the text you selected, is transferred to that service. You have the right to access, rectify, erase and object: write to globalcode01@gmail.com and you will get an answer within 30 days. You may also complain to your data protection authority (in Turkey, the Personal Data Protection Board). Before each of these transfers abroad the app asks for your explicit consent, with accept and decline offered equally. If you decline, nothing is sent and only that feature stays off; the startup settings file and ads are not loaded without consent either. You can give or withdraw consent any time in Settings › Privacy › Transfers abroad. Legal basis: explicit consent for transfers abroad (KVKK art. 5/1 and 9; GDPR art. 6(1)(a) and 49(1)(a)); for data kept on your device to run the app, performance of the contract (KVKK art. 5/2-c; GDPR art. 6(1)(b)). Data is collected by automated means while you use the app."""

PRIVACY_TR = """AllFixDoc Gizlilik Politikası
Son güncelleme: 8 Kasım 2026

AllFixDoc bir PDF okuyucu ve düzenleyicidir. Bu politika, uygulamanın hangi verileri neden işlediğini açıklar.

1. Belgelerin
AllFixDoc yalnızca senin seçtiğin dosyaları açar (Android dosya seçicisi ya da "Birlikte aç" ile). Depolama izni istemez, cihazını taramaz. Belgeler cihazında işlenir ve uygulama tarafından yüklenmez; tek istisna, AI asistanını kullandığında 4. maddede anlatılan durumdur.

2. Cihazında saklanan veriler
Uygulama şunları saklar: son açılan dosyaların listesi ve küçük önizleme görselleri, yer imleri ve okuma konumları, OCR ile tanınan metinler, çizdiğin imzalar, uygulama ayarları ve eklediysen seçtiğin AI servisinin API anahtarı (cihazının güvenli donanımındaki bir anahtarla şifrelenmiş olarak). Bu verileri Ayarlar'dan ya da uygulamanın depolama alanını temizleyerek silebilirsin. Sunum modunda yazdığın konuşmacı notlarını ve açtığın sunumlardan çıkarılan video ile sesleri de saklar; bunlar yedeklenmez.

3. Yedekleme
Android yedeklemesi açıksa Android; ayarlarını, yer imlerini ve okuma konumlarını Google hesabına yedekleyebilir. API anahtarın, imzaların, OCR sonuçları, önizleme görselleri ve son açılanlar listesi yedeklemeye dahil edilmez. İstersen yedek dosyasını kendin de dışa ve içe aktarabilirsin.

4. AI asistanı (isteğe bağlı)
AI asistanı yalnızca seçtiğin servis için bir API anahtarı eklersen çalışır: Google Gemini (varsayılan), Anthropic Claude, Groq, Mistral, OpenRouter ya da kendin eklediğin başka bir servis. Soru sorduğunda ya da özet istediğinde, seçtiğin sayfaların metni ve mesajların senin anahtarınla, şifreli bağlantı üzerinden yalnızca o servise gönderilir. Servis bu verileri kendi koşulları ve gizlilik politikası (ör. policies.google.com, anthropic.com/legal) kapsamında işler. Anahtarlar cihazında şifreli saklanır. AllFixDoc'un geliştiricisi bu verilere erişmez. Konuşarak not yazma, cihazının konuşma tanıma hizmetini (ör. Google) kullanır; AllFixDoc ses kaydetmez ve saklamaz.

5. Metin tanıma, kod okuma ve tarama
OCR, QR ve barkod okuma ile belge tarama, Google Play hizmetleri üzerinden Google ML Kit'i kullanır. Görüntüler cihazında işlenir. Google Play hizmetleri bu özelliklerle ilgili tanılama ve kullanım bilgilerini Google'ın gizlilik politikası kapsamında toplayabilir. Telefonunun dili uygulamada yoksa otomatik çeviri, Google ML Kit çeviri modelini bir kez (Wi‑Fi'de) indirir ve arayüzü cihazında çevirir; hiçbir metin cihazdan çıkmaz.

6. Reklamlar (ücretsiz sürüm)
Ücretsiz sürüm, Google AdMob üzerinden Ana sayfa, Dosyalar ve Araçlar ekranlarının altında banner reklam, bir araç işini bitirdiğinde de ara sıra tam ekran reklam gösterir. Belge okurken ya da düzenlerken reklam gösterilmez. Avrupa Ekonomik Alanı ve Birleşik Krallık'ta önce iznin istenir; tercihini Ayarlar'dan değiştirebilirsin. AdMob, reklamları göstermek ve ölçmek için reklam kimliği gibi cihaz tanımlayıcılarını, IP adresinden çıkarılan yaklaşık konumu ve reklam etkileşimlerini toplayabilir. Ayrıntılar: policies.google.com/technologies/ads.

7. Satın almalar
Reklamsız Pro sürümü satın alırsan ödeme Google Play tarafından işlenir. Uygulama yalnızca satın almanın etkin olup olmadığını öğrenir.

8. Çocuklar
AllFixDoc 13 yaşından küçük çocuklara yönelik değildir.

9. Değişiklikler
Bu politika değiştiğinde bu sayfa ve yukarıdaki tarih güncellenir.

10. İletişim
Bu politikayla ilgili soruların için uygulamanın Google Play sayfasındaki geliştirici iletişim adresini kullanabilirsin.

11. KVKK ve GDPR
Veri sorumlusu: Global Code 01 (globalcode01@gmail.com). Geliştirici belgelerini ve kişisel verilerini toplamaz; yalnızca bize yazarsan e-posta adresini ve mesajını yanıt vermek için işler. Uygulama açılırken geliştiricinin sitesinden (globalcode01-source.github.io, GitHub üzerinde) küçük bir ayar dosyası indirir; bu istekte IP adresi dışında veri gitmez. Google (AdMob, ML Kit, Play), GitHub ve AI asistanı için seçtiğin servis (Google, Anthropic, Groq, Mistral, OpenRouter vb.) yurt dışındaki sunucularda çalışır; bu özellikleri kullandığında IP adresin, AI asistanında ayrıca seçtiğin metin o hizmete yurt dışına aktarılır (KVKK m.9). KVKK m.11 ve GDPR uyarınca verilerinin işlenip işlenmediğini öğrenme, bilgi isteme, düzeltme, silme ve itiraz etme hakların vardır: globalcode01@gmail.com adresine yaz, en geç 30 gün içinde yanıtlanır. Yanıttan memnun kalmazsan Kişisel Verileri Koruma Kurulu'na (AB'de kendi veri koruma otoritene) şikâyette bulunabilirsin. Bu yurt dışı aktarımların her biri için, aktarımdan önce açık rızan istenir; kabul ve ret eşit seçenek olarak sunulur. Kabul etmezsen hiçbir veri gönderilmez, yalnızca o özellik kapalı kalır; açılıştaki ayar dosyası ve reklamlar da rıza olmadan yüklenmez. Rızanı istediğin zaman Ayarlar › Gizlilik › Yurt dışına aktarım izinleri bölümünden verebilir ya da geri alabilirsin. Hukuki sebepler: yurt dışı aktarımlar için açık rıza (KVKK m.5/1 ve m.9; GDPR m.6/1-a ve m.49/1-a); uygulamanın çalışması için cihazında saklanan veriler için sözleşmenin ifası (KVKK m.5/2-c; GDPR m.6/1-b). Veriler, uygulamayı kullanırken otomatik yollarla toplanır."""


def esc(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')
    text = text.replace("\n", "\\n")
    if text.startswith("@") or text.startswith("?"):
        text = "\\" + text
    return text


import importlib.util
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# Çeviri dosyası → kaynak klasörü (Endonezce eski Android sürümleri için "in")
QUALIFIERS = {
    "es": "es", "pt_BR": "pt-rBR", "fr": "fr", "de": "de", "it": "it", "ru": "ru", "ar": "ar",
    "hi": "hi", "id": "in", "ja": "ja", "zh_CN": "zh-rCN", "az": "az",
}

PLACEHOLDER = re.compile(r"%(?:\d+\$)?[sdf]|%%")


# Uygulama adı: Türkçe'de ayrı, diğer bütün dillerde İngilizce ad. Ad değişirse buradan ve metinlerden değişir.
APP_NAME_EN = "AllFixDoc"
APP_NAME_TR = "AllFixDoc"


def write(path: str, values: dict, privacy: str, app_name: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = ['<?xml version="1.0" encoding="utf-8"?>', "<resources>"]
    lines.append(f'    <string name="app_name">{esc(app_name)}</string>')
    for key in S:
        if key in values:
            lines.append(f'    <string name="{key}">{esc(values[key])}</string>')
    lines.append(f'    <string name="privacy_body">{esc(privacy)}</string>')
    lines.append("</resources>")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, "translations", name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.T, module.PRIVACY


def main():
    english = {k: v[0] for k, v in S.items()}
    write(f"{RES}/values/strings.xml", english, PRIVACY_EN, APP_NAME_EN)
    write(f"{RES}/values-tr/strings.xml", {k: v[1] for k, v in S.items()}, PRIVACY_TR, APP_NAME_TR)
    errors = []
    for name, qualifier in QUALIFIERS.items():
        if not os.path.exists(os.path.join(HERE, "translations", name + ".py")):
            continue
        table, privacy = load(name)
        for key, text in table.items():
            if key not in english:
                errors.append(f"{name}: bilinmeyen anahtar {key}")
            elif sorted(PLACEHOLDER.findall(text)) != sorted(PLACEHOLDER.findall(english[key])):
                errors.append(f"{name}: {key} yer tutucuları farklı")
        missing = [k for k in english if k not in table]
        write(f"{RES}/values-{qualifier}/strings.xml", table, privacy, APP_NAME_EN)
        print(f"{name}: {len(table)} metin" + (f", {len(missing)} eksik (İngilizce gösterilir)" if missing else ""))
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    # Otomatik çeviri (uygulamada olmayan diller) için kaynak İngilizce metinler
    assets = os.path.join(RES, "..", "assets", "i18n")
    os.makedirs(assets, exist_ok=True)
    import json
    with open(os.path.join(assets, "source.json"), "w", encoding="utf-8") as f:
        json.dump(sorted(set([APP_NAME_EN] + list(english.values()) + [PRIVACY_EN])), f, ensure_ascii=False)
    print(len(S) + 1, "strings written per language")


if __name__ == "__main__":
    main()
