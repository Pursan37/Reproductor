function ArtistaViewModel() {
	var self = this;
	self.id = ko.observable(0);
	self.nombre = ko.observable('');

	self.url=path_principal+'/api/';
	self.listado=ko.observableArray([]);
	self.mensaje=ko.observable('');
            
   	self.filtro_artista={
        dato:ko.observable(''),
        id:ko.observable(''),
    };

    self.artistaVO={
        id:ko.observable(0),
        nombre:ko.observable('').extend({ required: { message: ' Digite el nombre del proyecto.' } }),
        

     };
    
/*    self.paginacion = {
        pagina_actual: ko.observable(1),
        total: ko.observable(0),
        maxPaginas: ko.observable(5),
        directiones: ko.observable(true),
        limite: ko.observable(true),
        cantidad_por_paginas: ko.observable(0),
        text: {
            first: ko.observable('Inicio'),
            last: ko.observable('Fin'),
            back: ko.observable('<'),
            forward: ko.observable('>')
        }
    };*/

    self.limpiar=function(){                  
        self.artistaVO.id(0);
        self.artistaVO.nombre('');
    }     
    self.guardar=function(){

        if (ArtistaViewModel.errores_artista().length == 0) {//se activa las validaciones
            if(self.artistaVO.id()==0){
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
                     url: self.url+'artista/',//url api
                     parametros:self.artistaVO                        
                };
                //parameter =ko.toJSON(self.contratistaVO);
                RequestFormData(parametros);
            }else{                 
                  var parametros={     
                        metodo:'PUT',
                       callback:function(datos, estado, mensaje){
                            if (estado=='success') {
                              $("#mensajeExito").html(mensaje);
                              $("#mensajeError").hide();
                              $("#mensajeExito").show();
                            }else{
                              $("#mensajeError").html(mensaje);
                              $("#mensajeError").show();
                              $("#mensajeExito").hide();                               
                            } 
                       },//funcion para recibir la respuesta 
                       url: self.url+'artista/'+ self.artistaVO.id()+'/',
                       parametros:self.artistaVO                        
                  };
                  RequestFormData(parametros);
            }
        } else {
             ArtistaViewModel.errores_artista.showAllMessages();//mostramos las validacion
        }
    }

	self.consultar = function(pagina){
		if (pagina > 0){
			self.filtro_artista.dato($('#txtBuscar').val());
			path = self.url+'artista/?format=json';
            parameter = { dato: self.filtro_artista.dato(),
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
            self.filtro_artista.dato($('#txtBuscar').val());
            self.consultar(1);
        }
        return true;
    }

  self.eliminarArtista = function (idArtista) {
   // alert('eliminando el id ' + idArtista);
    var path =self.url+'artista/'+idArtista+'/';
             var parameter = {};
             RequestAnularOEliminar("Esta seguro que desea eliminar este artista?", path, parameter, function () {                 
                 self.consultar(1);
             })
  }
}

var artista = new ArtistaViewModel();

ArtistaViewModel.errores_artista = ko.validation.group(artista.artistaVO);

ko.applyBindings(artista);