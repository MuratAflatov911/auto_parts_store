def cart_item_count(request):
    count=0
    if request.user.is_authenticated:
        c=getattr(getattr(request.user,'cart',None),'items',None)
        if c: count=sum(i.quantity for i in c.all())
    return {'cart_item_count':count}
