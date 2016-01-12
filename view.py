from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Stock
from yahoo_finance import Share
from django.template import Context
from .forms import addStockForm
from django.views.generic.edit import CreateView

# Create your views here.
@login_required
def home(request):
    return render(request,'stock/home.html')

@login_required
def stockView(request):
    context=Context()
    context['stocks']=[]
    stocks=Stock.objects.all()
    for stock in stocks:
        if stock.purchaser==request.user:
            context['stocks'].append({'id':stock.id,'symbol':stock.symbol,'qty':stock.qty,'price':(Share(stock.symbol)).get_price()})
    return render(request,'stock/stock_list.html',context)

def addStock(request):
    form=addStockForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        stock=Stock.objects.create(symbol=instance.symbol,qty=instance.qty,purchaser=request.user)
    return render(request,'stock/add_stock.html',{'form':form})

class StockCreate(CreateView):
    model=Stock
    fields=['symbol','qty']
    template_name='stock/add_stock.html'

    def form_valid(self,form):
        form.instance.purchaser=self.request.user
        return super(StockCreate,self).form_valid(form)
