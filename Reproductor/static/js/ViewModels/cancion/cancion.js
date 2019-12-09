function CancionViewModel() {
	var self = this;
	self.id = ko.observable(0);
	self.titulo = ko.observable('');
    self.track_file = ko.observable('');    
    self.artista = ko.observable('');
    self.album = ko.observable('');

	self.url=path_principal+'/api/';
	self.listado=ko.observableArray([]);
	self.mensaje=ko.observable('');

   	self.filtro_cancion={
        dato:ko.observable(''),
        id:ko.observable(''),
    };

	self.consultar = function(pagina){
		if (pagina > 0){
			self.filtro_cancion.dato($('#txtBuscar').val());
			path = self.url+'cancion/?format=json';
            parameter = { dato: self.filtro_cancion.dato(),
                          page: pagina 
                        };
            RequestGet(function (datos, estado, mensage) {
                if (datos!=null && datos.length > 0) {

                    self.listado(datos); 
                    self.mensaje('');
                } else {
                    self.listado([]);
                    self.mensaje(mensajeNoFound);//mensaje not found se encuentra el el archivo call-back.js
                }
                cerrarLoading();
            }, path, parameter,undefined,false);
		}

	}
    self.consulta_enter = function (d,e) {
        if (e.which == 13) {
            self.filtro_cancion.dato($('#txtBuscar').val());
            self.consultar(1);
        }
        return true;
    }    
}

var cancion = new CancionViewModel();
ko.applyBindings(cancion);

ko.bindingHandlers.audio = {
    init: function (element, valueAccessor) {
        var config = ko.unwrap(valueAccessor());
        var file = config.sound;
        var observable = config.value;
        observable.subscribe(function () {
            var audio = new Audio(file);
            audio.play();
        });
    }
};
