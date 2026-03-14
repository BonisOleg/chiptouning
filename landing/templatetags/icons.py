from django import template
from django.utils.safestring import mark_safe

register = template.Library()

ICONS = {
    'shield': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 '
        '11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 '
        '9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/>'
        '</svg>'
    ),
    'chart': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941"/>'
        '</svg>'
    ),
    'clock': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/>'
        '</svg>'
    ),
    'key': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 '
        '17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 '
        '.43-1.563A6 6 0 1121.75 8.25z"/>'
        '</svg>'
    ),
    'eye': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 '
        '8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 '
        '0-8.573-3.007-9.963-7.178z"/>'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>'
        '</svg>'
    ),
    'checkmark': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>'
        '</svg>'
    ),
    'star': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04 '
        '.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 '
        '0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 '
        '0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"/>'
        '</svg>'
    ),
    'map': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/>'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/>'
        '</svg>'
    ),
    'phone': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/>'
        '</svg>'
    ),
    'email': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/>'
        '</svg>'
    ),
    'location': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/>'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/>'
        '</svg>'
    ),
    'external': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"/>'
        '</svg>'
    ),
    'arrow-right': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>'
        '</svg>'
    ),
    'check': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/>'
        '</svg>'
    ),
    'warning': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z"/>'
        '</svg>'
    ),
    # -- Automotive / chip-tuning icons --
    'engine': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M11.42 15.17L17.25 21A2.652 2.652 0 0021 17.25l-5.877-5.877M11.42 15.17l2.496-3.03c.317-.384.74-.626 1.208-.766M11.42 15.17l-4.655 5.653a2.548 2.548 0 11-3.586-3.586l6.837-5.63m5.108-.233c.55-.164 1.163-.188 1.743-.14a4.5 4.5 0 004.486-6.336l-3.276 3.277a3.004 3.004 0 01-2.25-2.25l3.276-3.276a4.5 4.5 0 00-6.336 4.486c.091 1.076-.071 2.264-.904 2.95l-.102.085"/>'
        '</svg>'
    ),
    'speed': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/>'
        '</svg>'
    ),
    'fuel': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M15.362 5.214A8.252 8.252 0 0112 21 8.25 8.25 0 016.038 7.048 8.287 8.287 0 009 9.6a8.983 8.983 0 013.361-6.867 8.21 8.21 0 003 2.48z"/>'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 18a3.75 3.75 0 00.495-7.467 5.99 5.99 0 00-1.925 3.546 5.974 5.974 0 01-2.133-1.001A3.75 3.75 0 0012 18z"/>'
        '</svg>'
    ),
    'wrench': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M21.75 6.75a4.5 4.5 0 01-4.884 4.484c-1.076-.091-2.264.071-2.95.904l-7.152 8.684a2.548 2.548 0 11-3.586-3.586l8.684-7.152c.833-.686.995-1.874.904-2.95a4.5 4.5 0 016.336-4.486l-3.276 3.276a3.004 3.004 0 002.25 2.25l3.276-3.276c.256.565.398 1.192.398 1.852z"/>'
        '<path stroke-linecap="round" stroke-linejoin="round" d="M4.867 19.125h.008v.008h-.008v-.008z"/>'
        '</svg>'
    ),
    'power': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/>'
        '</svg>'
    ),
    'headset': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155"/>'
        '</svg>'
    ),
    'filter': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 3c2.755 0 5.455.232 8.083.678.533.09.917.556.917 1.096v1.044a2.25 2.25 0 01-.659 1.591l-5.432 5.432a2.25 2.25 0 00-.659 1.591v2.927a2.25 2.25 0 01-1.244 2.013L9.75 21v-6.568a2.25 2.25 0 00-.659-1.591L3.659 7.409A2.25 2.25 0 013 5.818V4.774c0-.54.384-1.006.917-1.096A48.32 48.32 0 0112 3z"/>'
        '</svg>'
    ),
    'recycle': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 00-3.7-3.7 48.678 48.678 0 00-7.324 0 4.006 4.006 0 00-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3l-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 003.7 3.7 48.656 48.656 0 007.324 0 4.006 4.006 0 003.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3l-3 3"/>'
        '</svg>'
    ),
    'droplet': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 21a9.004 9.004 0 006.366-2.634 9 9 0 10-12.732 0A9.004 9.004 0 0012 21zm0 0V3"/>'
        '</svg>'
    ),
    'gauge': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M10.5 6a7.5 7.5 0 107.5 7.5h-7.5V6z"/>'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M13.5 10.5H21A7.5 7.5 0 0013.5 3v7.5z"/>'
        '</svg>'
    ),
    'wind': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"/>'
        '</svg>'
    ),
    'alert': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z"/>'
        '</svg>'
    ),
    'telegram': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" '
        'fill="currentColor" aria-hidden="true">'
        '<path d="M11.944 0A12 12 0 000 12a12 12 0 0012 12 12 12 0 0012-12A12 12 0 0012 0h-.056zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 01.171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.479.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>'
        '</svg>'
    ),
    'viber': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" '
        'fill="currentColor" aria-hidden="true">'
        '<path d="M11.398.002C9.473.028 5.331.344 3.014 2.467 1.294 4.187.539 6.681.36 9.788.181 12.895.125 18.52 5.564 19.922v2.382s-.038.964.599 1.159c.637.196 1.013-.41 1.624-1.063.336-.357.798-.882 1.149-1.283 3.167.267 5.603-.343 5.88-.432.64-.207 4.263-.672 4.857-5.49.613-4.961-.295-8.1-1.943-9.511l-.001-.002c-.462-.432-2.327-1.932-6.673-2.083 0 0-.329-.026-.658-.022zm.099 1.68c.276-.004.532.016.532.016 3.678.128 5.272 1.35 5.655 1.71h.002c1.354 1.166 2.085 3.943 1.578 8.137-.488 3.967-3.378 4.255-3.918 4.43-.228.073-2.385.61-5.146.437 0 0-2.04 2.464-2.677 3.103-.1.1-.214.139-.291.12-.109-.029-.139-.155-.137-.344 0-.128.008-3.098.008-3.098C6.396 14.843 6.4 10.099 6.54 7.77c.14-2.43.728-4.41 2.155-5.778 1.34-1.281 2.527-1.301 2.8-1.31zm.2 2.272a.351.351 0 00-.356.346.352.352 0 00.346.357c1.025.012 1.86.396 2.474 1.053.618.661.949 1.59.96 2.638a.352.352 0 00.352.346h.006a.351.351 0 00.346-.358c-.014-1.235-.41-2.352-1.175-3.168-.757-.81-1.803-1.266-3-.1214h.047zm-2.843 1.32c-.176-.004-.36.046-.5.208l-.628.652c-.187.197-.299.44-.279.729.044.624.397 1.904 1.545 3.073 1.488 1.514 3.265 2.136 3.265 2.136s.247.092.41.026c.163-.066.284-.237.284-.237l.502-.734c.274-.4.004-.852-.44-1.075l-1.398-.63c-.31-.142-.645-.013-.803.186l-.357.429s-.684-.122-1.418-.856c-.735-.735-.856-1.418-.856-1.418l.429-.357c.199-.158.328-.493.186-.803l-.63-1.398c-.16-.32-.412-.517-.712-.53h-.6zm5.098.572a.35.35 0 00-.321.376c.055.627.009.94-.183 1.456a.351.351 0 00.197.456.354.354 0 00.456-.197c.243-.654.295-1.094.228-1.862a.35.35 0 00-.377-.229z"/>'
        '</svg>'
    ),
    'whatsapp': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" '
        'fill="currentColor" aria-hidden="true">'
        '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
        '</svg>'
    ),
    'instagram': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" '
        'fill="currentColor" aria-hidden="true">'
        '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>'
        '</svg>'
    ),
    'scroll-down': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" d="M19.5 13.5L12 21m0 0l-7.5-7.5M12 21V3"/>'
        '</svg>'
    ),
    'globe': (
        '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75" aria-hidden="true">'
        '<path stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418"/>'
        '</svg>'
    ),
}


@register.simple_tag
def icon(name, **kwargs):
    svg = ICONS.get(name, ICONS['checkmark'])
    return mark_safe(svg)


@register.filter
def nl2li(value):
    """Convert newline-separated text to HTML list items."""
    lines = [line.strip() for line in value.split('\n') if line.strip()]
    items = ''.join(f'<li>{line}</li>' for line in lines)
    return mark_safe(f'<ul>{items}</ul>')
