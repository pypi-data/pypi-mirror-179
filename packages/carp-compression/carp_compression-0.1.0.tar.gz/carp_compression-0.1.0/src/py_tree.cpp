#include "tree_class.hpp"
#include "helper.hpp"

vec vector2vec(vector<double>& vector_old){
    vec vec_new(vector_old.size());
    int i = 0;
    for(double& n: vector_old){
        vec_new(i) = n;
        //printf(n)
        i++;
    }
    return vec_new;
}

uvec vector2uvec(vector<double>& vector_old){
    vec vec_new = vector2vec(vector_old);
    uvec uvec_new = conv_to<uvec>::from( vec_new );
    return uvec_new;
}

mat vector2mat(vector<vector<double>>& vector_old){
    int M = vector_old.size();
    int N = vector_old[0].size();
    mat mat_new(M,N);
    int i = 0;
    for(vector<double>& m: vector_old){
        int j = 0;
        for(double& n: m){
            mat_new(i,j) = n;
            j++;
        }
        i++;
    }
    return mat_new;
}

vector<double> vec2vector(vec& vec_old){
    vector<double> vector_new;
    for(double& n: vec_old){
        vector_new.push_back(n);
    }
    return vector_new;
}

vector<double> uvec2vector(uvec& uvec_old){
    vec vec_old = conv_to<vec>::from( uvec_old );
    vector<double> vector_new = vec2vector(vec_old);
    return vector_new;
}

vector<vector<double>> mat2vector(mat& mat_old){
    vector<vector<double>> vector_new;
    for(int i = 0; i < mat_old.n_rows; i++){
        vector<double> vector_row;
        for(int j = 0; j < mat_old.n_cols; j++){
            vector_row.push_back(mat_old(i,j));
        }
        vector_new.push_back(vector_row);
    }
    return vector_new;
}

vector<vector<double>> umat2vector(umat& umat_old){
    mat mat_old = conv_to<mat>::from( umat_old );
    vector<vector<double>> vector_new;
    for(int i = 0; i < mat_old.n_rows; i++){
        vector<double> vector_row;
        for(int j = 0; j < mat_old.n_cols; j++){
            vector_row.push_back(mat_old(i,j));
        }
        vector_new.push_back(vector_row);
    }
    return vector_new;
}

vector<vector<double>> get_par(vector<double>& obs, vector<double>& dimension, vector<double>& hyper){
    vec obs_vec = vector2vec(obs);
    uvec dimension_vec = vector2uvec(dimension);
    vec hyper_vec = vector2vec(hyper);
    class_tree tree_test(obs_vec, dimension_vec);
    mat par_mat = tree_test.hyper2par(hyper_vec);
    vector<vector<double>> par = mat2vector(par_mat);
    return par;
}

vector<double> get_lambda_map(vector<double>& obs, vector<double>& dimension, vector<double>& hyper){
    vec obs_vec = vector2vec(obs);
    uvec dimension_vec = vector2uvec(dimension);
    vec hyper_vec = vector2vec(hyper);
    class_tree tree_test(obs_vec, dimension_vec);
    mat par = tree_test.hyper2par(hyper_vec);
    tree_test.get_post_map(par);
    vec lambda_map_vec = tree_test.get_lambda_map();
    vector<double> lambda_map = vec2vector(lambda_map_vec);
    return lambda_map;
}

vector<vector<double>> get_left_child(vector<double>& obs, vector<double>& dimension){
    vec obs_vec = vector2vec(obs);
    uvec dimension_vec = vector2uvec(dimension);
    class_tree tree_test(obs_vec, dimension_vec);
    umat left_child = tree_test.get_left_child();
    vector<vector<double>> rank_left_child = umat2vector(left_child);
    return rank_left_child;
}

vector<vector<double>> get_right_child(vector<double>& obs, vector<double>& dimension){
    vec obs_vec = vector2vec(obs);
    uvec dimension_vec = vector2uvec(dimension);
    class_tree tree_test(obs_vec, dimension_vec);
    umat right_child = tree_test.get_right_child();
    vector<vector<double>> rank_right_child = umat2vector(right_child);
    return rank_right_child;
}

vector<vector<double>> get_dividible(vector<double>& obs, vector<double>& dimension){
    vec obs_vec = vector2vec(obs);
    uvec dimension_vec = vector2uvec(dimension);
    class_tree tree_test(obs_vec, dimension_vec);
    umat dividible_mat = tree_test.get_dividible();
    vector<vector<double>> dividible = umat2vector(dividible_mat);
    return dividible;
}

vector<double> get_y(vector<double>& obs, vector<double>& dimension){
    vec obs_vec = vector2vec(obs);
    uvec dimension_vec = vector2uvec(dimension);
    class_tree tree_test(obs_vec, dimension_vec);
    vec y_vec = tree_test.get_y();
    vector<double> y = vec2vector(y_vec);
    return y;
}

vector<vector<double>> get_MAP(vector<double>& obs, vector<double>& dimension, vector<double>& hyper){
    vec obs_vec = vector2vec(obs);
    uvec dimension_vec = vector2uvec(dimension);
    vec hyper_vec = vector2vec(hyper);
    class_tree tree_test(obs_vec, dimension_vec);
    mat par = tree_test.hyper2par(hyper_vec);
        
    tree_test.get_post_map(par);
    tree_test.get_lambda_mat();
        
    tree_test.fit_MAP_tree(par);
        
    umat MAP_tree = tree_test.MAP_tree;
    vector<vector<double>> MAP = umat2vector(MAP_tree);
    return MAP;
}




PYBIND11_MODULE(py_tree, m){
    m.def("get_par",&get_par);
    m.def("get_lambda_map",&get_lambda_map);
    m.def("get_left_child",&get_left_child);
    m.def("get_right_child",&get_right_child);
    m.def("get_dividible",&get_dividible);
    m.def("get_y",&get_y);
    m.def("get_MAP",&get_MAP);
    //py::class_<py_tree>(m, "py_tree")
        //.def(py::init<const vec &, uvec &>())
        //.def("get_lambda_map", &py_tree::get_lambda_map);
}
