from django import template
from django.urls import reverse, NoReverseMatch
from tree_menu_app.models import Menu

register = template.Library()

@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    try:
        menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    all_items = list(menu.items.all())

    item_dict = {item.id: item for item in all_items}

    active_item = None
    for item in all_items:
        if current_path.startswith(item.get_url()):
            active_item = item
            break

    open_ids = set()
    def collect_parents(item):
        if item and item.id not in open_ids:
            open_ids.add(item.id)
            if item.parent_id:
                collect_parents(item_dict.get(item.parent_id))

    if active_item:
        collect_parents(active_item)

    def build_tree(parent=None, depth=0):
        tree = []
        for item in all_items:
            if item.parent_id == (parent.id if parent else None):
                node = {
                    'item': item,
                    'children': [],
                    'is_open': item.id in open_ids,
                    'is_active': item == active_item,
                }
                if node['is_open'] or depth == 0:
                    node['children'] = build_tree(item, depth + 1)
                tree.append(node)
        return tree

    menu_tree = build_tree()
    return {'menu_tree': menu_tree}
