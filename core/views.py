from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class MinimumCostAPIView(APIView):
    '''
    solves warehouse problem, return minimum cost
    '''

    def get_cost(self, weight):
        if weight>0:    
            cost = 10
            weight = weight - 5
            if weight>0:
                temp = weight//5
                cost += (temp*8)
                weight = weight - (temp*5)
                if weight!=0:
                    cost += 8	
            return cost
        return 0	


    def get_cost_per_centre(self, a, b, c, d, e, f, g, h, i):
        weight = {}
        weight['a'] = 3
        weight['b'] = 2
        weight['c'] = 8
        weight['d'] = 12
        weight['e'] = 25
        weight['f'] = 15
        weight['g'] = 0.5
        weight['h'] = 1
        weight['i'] = 2

        c1 = (weight['a']*a) + (weight['b']*b) + (weight['c']*c)
        c2 = (weight['d']*d) + (weight['e']*e) + (weight['f']*f)
        c3 = (weight['g']*g) + (weight['h']*h) + (weight['i']*i)
        print('weight_c1-',c1)
        print('weight_c2-',c2)
        print('weight_c3-',c3)
        c1_cost = int(self.get_cost(c1))
        c2_cost = int(self.get_cost(c2))
        c3_cost = int(self.get_cost(c3))
        return [c1_cost, c2_cost, c3_cost]  


    def get_total_cost(self, c1, c2, c3):
        if (c1==0 and c2==0 and c3==0):
            return 0  
        
        elif (c1!=0 and c2==0 and c3==0): # c1
            return (c1*3)
        
        elif(c1==0 and c2!=0 and c3==0): # c2
            return (c2*2.5)
        
        elif(c1==0 and c2==0 and c3!=0): # c3
            return (c3*2)

        elif(c1!=0 and c2!=0 and c3==0): # c1 c2
            return ((c1*3) + 25 + (2.5*c2))

        elif(c1==0 and c2!=0 and c3!=0): # c2 c3
            return ((c2*2.5) + 20 + (2*c3))

        elif(c1!=0 and c2==0 and c3!=0): # c1 c3
            return ((c1*3) + 20 + (c3*2))

        else: # c1 c2 c3
            return ((c1*3) + 25 + (c2*2.5) + 20 + (c3*2))


    def calculate(self, a, b , c, d, e, f, g, h, i):
        cost = self.get_cost_per_centre(a,b,c,d,e,f,g,h,i)
        c1 = cost[0]
        c2 = cost[1]
        c3 = cost[2]
        print("c1- ",c1)
        print("c2- ",c2)
        print("c3- ",c3)

        total = self.get_total_cost(c1,c2,c3)
        return total


    def get(self, request, *args, **kwargs):
        try:
            a = int(request.query_params.get('a'))
            b = int(request.query_params.get('b'))
            c = int(request.query_params.get('c'))
            d = int(request.query_params.get('d'))
            e = int(request.query_params.get('e'))
            f = int(request.query_params.get('f'))
            g = int(request.query_params.get('g'))
            h = int(request.query_params.get('h'))
            i = int(request.query_params.get('i'))
            
            print(a,b,c,d,e,f,g,h,i)
            cost = self.calculate(a,b,c,d,e,f,g,h,i)

            return Response({
                    'status': True,
                    'minimum cost': cost}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False,
                             'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)      