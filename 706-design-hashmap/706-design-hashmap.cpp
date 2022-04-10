class MyHashMap {
public:
    MyHashMap() {
        std::map<int, int> *myhashmap=nullptr;

    }
    
    void put(int key, int value) {
 myhashmap[key]=value;
    }
    
    int get(int key) {
        if (myhashmap.find(key)==myhashmap.end()) return -1;
        else return myhashmap[key];
    }
    
    void remove(int key) {
        
        myhashmap.erase(key);
        
    }
private:
        std::map<int, int> myhashmap;
        std::pair<std::map<int, int>::iterator, bool> ret;
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */