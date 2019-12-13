function CancionViewModel() {
	var self = this;
	self.id = ko.observable(0);
	self.titulo = ko.observable('');
    self.track_file = ko.observable('');    
    self.album = ko.observable('');

	self.url=path_principal+'/api/';
	self.listado=ko.observableArray([]);
	self.mensaje=ko.observable('');

    self.listado_albums = ko.observableArray([]);

   	self.filtro_cancion={
        dato:ko.observable(''),
        id:ko.observable(''),
    };

    self.cancionVO={
        id:ko.observable(0),
        titulo:ko.observable('').extend({ required: { message: ' Digite el titulo de la cancion.' } }),
        track_file:ko.observable('').extend({ required: { message: ' Ingrese un archivo.' } }),
        album_id:ko.observable('').extend({ required: { message: ' Selecione el album.' } })

    };

    self.limpiar=function(){                  
        self.cancionVO.id(0);
        self.caniconVO.titulo('');
        self.cancionVO.track_file('');
        self.cancionVO.artista_id('');
    }

    self.guardar=function(){

        if (CancionViewModel.errores_cancion().length == 0) {//se activa las validaciones
            if(self.cancionVO.id()==0){
                alert(cancionVO);
                var parametros={                     
                     callback:function(datos, estado, mensaje){  
                        if (estado=='success') {
                            self.limpiar();
                            $("#mensajeExito").html(mensaje);
                            $("#mensajeError").hide();
                            $("#mensajeExito").show();
                        }else{
                            $("#mensajeError").html(mensaje);
                            $("#mensajeError").show();
                            $("#mensajeExito").hide();                          
                        }                     
                     },//funcion para recibir la respuesta 
                     url: self.url+'cancion/',//url api
                     parametros:self.cancionVO                        
                };
                //parameter =ko.toJSON(self.contratistaVO);
                RequestFormData(parametros);
            }else{                 
                  var parametros={     
                        metodo:'PUT',                
                       callback:function(datos, estado, mensaje){
                            if (estado=='success') {
                              self.filtro_cancion("");
                              self.consultar(1);
                      /*        $('#modal_acciones').modal('hide');*/
                              self.limpiar();
                            } 
                       },//funcion para recibir la respuesta 
                       url: self.url+'cancion/'+ self.cancionVO.id()+'/',
                       parametros:self.cancionVO                        
                  };
                  RequestFormData(parametros);
            }
        } else {
             CancionViewModel.errores_cancion.showAllMessages();//mostramos las validacion
        }
    }  

    self.consultar_albums = function(pagina){
    if (pagina > 0){
      //self.filtro_album.dato($('#txtBuscar').val());
      path = self.url+'album/?format=json';
            parameter = {};
            RequestGet(function (datos, estado, mensage) {
                if (datos!=null && datos.length > 0) {
                    self.listado_albums(datos); 
                } else {
                    self.listado_albums([]);
                }
                cerrarLoading();
            }, path, parameter,undefined,false);
    }    
    }
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
    self.eliminarCancion = function (idCancion) {
   // alert('eliminando el id ' + idAlbum);
    var path =self.url+'cancion/'+idCancion+'/';
             var parameter = {};
             RequestAnularOEliminar("Esta seguro que desea eliminar esta cancion?", path, parameter, function () {                 
                 self.consultar(1);
             })
  }    
}

var cancion = new CancionViewModel();
CancionViewModel.errores_cancion = ko.validation.group(cancion.cancionVO);
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
