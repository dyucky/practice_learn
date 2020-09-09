#include <map>
#include <string>
#include <vector>

using namespace std;

class UndergroundSystem {
public:

struct origin
{
    origin(){}
    origin(string station, int time):
        oStation(station), oTime(time){}
    string oStation;
    int oTime;
};

    map<int, origin> inTransit;

    map<string, 
        map<string, vector<int> > > 
        commutes;

    UndergroundSystem() {

    }



    void checkIn(int id, string stationName, int t) {
        inTransit[id] = origin(stationName, t);
    }
    
    void checkOut(int id, string stationName, int t) {
        auto it = inTransit.find(id);
        if (it == inTransit.end() )
        { return; }
        string ostation = it->second.oStation;
        int time  = t - (it->second.oTime);
        commutes[ostation][stationName].push_back(time);
    }
    
    double getAverageTime(string startStation, string endStation) {
        if ( commutes.empty() )
        { return 0; }

        auto fromsta = commutes.find(startStation);
        if (fromsta == commutes.end())
        { return 0; }

        auto tosta = fromsta->second.find(endStation);
        if (tosta == fromsta->second.end() )
        { return 0; }

        vector<int>& commutes = tosta->second;
        if (!commutes.empty())
        {
            double trips = commutes.size();
            double total = 0;
            for (auto& it: commutes)
            {
                total += it ; 
            }
            return (total / trips);
        }

        return 0;
    }
};

int main()
{
    return 0;
}
/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */