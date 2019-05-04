//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var io = new extIO({
            functions: {
                js: 'nonUniqueElements',
                python: 'non_unique_elements'
            }
        });
        io.start();
    }
);
