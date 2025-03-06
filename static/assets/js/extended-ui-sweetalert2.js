/**
 * Sweet Alerts
 */

'use strict';

(function () {
  const basicAlert = document.querySelector('#basic-alert'),
    withTitle = document.querySelector('#with-title'),
    footerAlert = document.querySelector('#footer-alert'),
    htmlAlert = document.querySelector('#html-alert'),
    positionTopStart = document.querySelector('#position-top-start'),
    positionTopEnd = document.querySelector('#position-top-end'),
    positionBottomStart = document.querySelector('#position-bottom-start'),
    positionBottomEnd = document.querySelector('#position-bottom-end'),
    bounceInAnimation = document.querySelector('#bounce-in-animation'),
    fadeInAnimation = document.querySelector('#fade-in-animation'),
    flipXAnimation = document.querySelector('#flip-x-animation'),
    tadaAnimation = document.querySelector('#tada-animation'),
    shakeAnimation = document.querySelector('#shake-animation'),
    iconSuccess = document.querySelector('#type-success'),
    iconSave = document.querySelector('#type-save'),
    iconUpdate = document.querySelector('#type-update'),
    confirmDelete = document.querySelector('#confirm-delete'),
    sectionDelete = document.querySelector('#section-delete'),
    groupDelete = document.querySelector('#group-delete'),
    iconInfo = document.querySelector('#type-info'),
    iconWarning = document.querySelector('#type-warning'),
    iconError = document.querySelector('#type-error'),
    iconQuestion = document.querySelector('#type-question'),
    customImage = document.querySelector('#custom-image'),
    autoClose = document.querySelector('#auto-close'),
    outsideClick = document.querySelector('#outside-click'),
    progressSteps = document.querySelector('#progress-steps'),
    ajaxRequest = document.querySelector('#ajax-request'),
    confirmText = document.querySelector('#confirm-text'),
    submitText = document.querySelector('#submit-text'),
    updatedText = document.querySelector('#updated-text'),
    deleteText = document.querySelector('#delete-text'),
    updatedAlertText = document.querySelector('#updated-alert-text'),
    addsecText = document.querySelector('#add-sec-text'),
    updatedsecText = document.querySelector('#updated-sec-text'),
    addgrpText = document.querySelector('#add-grp-text'),
    updatedgrpText = document.querySelector('#updated-grp-text'),
    confirmColor = document.querySelector('#confirm-color');
    

  // Basic Alerts
  // --------------------------------------------------------------------

  // Default Alert
  if (basicAlert) {
    basicAlert.onclick = function () {
      Swal.fire({
        title: 'Any fool can use a computer',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Alert With Title
  if (withTitle) {
    withTitle.onclick = function () {
      Swal.fire({
        title: 'The Internet?,',
        text: 'That thing is still around?',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Alert With Footer
  if (footerAlert) {
    footerAlert.onclick = function () {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Something went wrong!',
        footer: '<a href>Why do I have this issue?</a>',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Html Alert
  if (htmlAlert) {
    htmlAlert.onclick = function () {
      Swal.fire({
        title: '<span class="fw-medium">HTML <u>example</u></span>',
        icon: 'info',
        html:
          'You can use <b>bold text</b>, ' +
          '<a href=" " target="_blank">links</a> ' +
          'and other HTML tags',
        showCloseButton: true,
        showCancelButton: true,
        focusConfirm: false,
        confirmButtonText: '<i class="ti ti-thumb-up"></i> Great!',
        confirmButtonAriaLabel: 'Thumbs up, great!',
        cancelButtonText: '<i class="ti ti-thumb-down"></i>',
        cancelButtonAriaLabel: 'Thumbs down',
        customClass: {
          confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
          cancelButton: 'btn btn-label-secondary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Alerts Positions
  // --------------------------------------------------------------------

  // Top Start Alert
  if (positionTopStart) {
    positionTopStart.onclick = function () {
      Swal.fire({
        position: 'top-start',
        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500,
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Top End Alert
  if (positionTopEnd) {
    positionTopEnd.onclick = function () {
      Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500,
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Bottom Start Alert
  if (positionBottomStart) {
    positionBottomStart.onclick = function () {
      Swal.fire({
        position: 'bottom-start',
        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500,
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Bottom End Alert
  if (positionBottomEnd) {
    positionBottomEnd.onclick = function () {
      Swal.fire({
        position: 'bottom-end',
        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500,
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Alerts With Animations
  // --------------------------------------------------------------------

  // Bounce In Animation
  if (bounceInAnimation) {
    bounceInAnimation.onclick = function () {
      Swal.fire({
        title: 'Bounce In Animation',
        showClass: {
          popup: 'animate__animated animate__bounceIn'
        },
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Fade In Animation
  if (fadeInAnimation) {
    fadeInAnimation.onclick = function () {
      Swal.fire({
        title: 'Fade In Animation',
        showClass: {
          popup: 'animate__animated animate__fadeIn'
        },
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Flip X Animation
  if (flipXAnimation) {
    flipXAnimation.onclick = function () {
      Swal.fire({
        title: 'Flip In Animation',
        showClass: {
          popup: 'animate__animated animate__flipInX'
        },
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Tada Animation
  if (tadaAnimation) {
    tadaAnimation.onclick = function () {
      Swal.fire({
        title: 'Tada Animation',
        showClass: {
          popup: 'animate__animated animate__tada'
        },
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Shake Animation
  if (shakeAnimation) {
    shakeAnimation.onclick = function () {
      Swal.fire({
        title: 'Shake Animation',
        showClass: {
          popup: 'animate__animated animate__shakeX'
        },
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Alert Types
  // --------------------------------------------------------------------

  // Success Alert
  if (iconSuccess) {
    iconSuccess.onclick = function () {
      Swal.fire({
        title: 'Good job!',
        text: 'You clicked the button!',
        icon: 'success',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }


    // Save Alert
    if (iconSave) {
      iconSave.onclick = function () {
        Swal.fire({
          title: 'Are you Sure?',
          text: 'New camera details will be saved',
          icon: 'success', 
        showCancelButton: true,
        confirmButtonText: 'Yes, Submit',
        customClass: {
          confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
          cancelButton: 'btn btn-label-secondary waves-effect waves-light'
        },
        buttonsStyling: false 
        });
      };
    }

    // Add Section
    if (addsecText) {
      addsecText.onclick = function () {
        Swal.fire({
          title: 'Are you Sure?',
          text: 'Section details will be added',
          icon: 'success', 
        showCancelButton: true,
        confirmButtonText: 'Yes, Proceed',
        customClass: {
          confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
          cancelButton: 'btn btn-label-secondary waves-effect waves-light'
        },
        buttonsStyling: false 
        });
      };
    }

        // Update Section
        if (updatedsecText) {
          updatedsecText.onclick = function () {
            Swal.fire({
              title: 'Are you Sure?',
              text: 'Section details will be updated',
              icon: 'success', 
            showCancelButton: true,
            confirmButtonText: 'Yes, Proceed',
            customClass: {
              confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
              cancelButton: 'btn btn-label-secondary waves-effect waves-light'
            },
            buttonsStyling: false 
            });
          };
        }

  
        // Add Group
        if (addgrpText) {
          addgrpText.onclick = function () {
            Swal.fire({
              title: 'Are you Sure?',
              text: 'Group details will be added',
              icon: 'success', 
            showCancelButton: true,
            confirmButtonText: 'Yes, Proceed',
            customClass: {
              confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
              cancelButton: 'btn btn-label-secondary waves-effect waves-light'
            },
            buttonsStyling: false 
            });
          };
        }


          // Update Group
          if (updatedgrpText) {
            updatedgrpText.onclick = function () {
              Swal.fire({
                title: 'Are you Sure?',
                text: 'Group details will be updated',
                icon: 'success', 
              showCancelButton: true,
              confirmButtonText: 'Yes, Proceed',
              customClass: {
                confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
                cancelButton: 'btn btn-label-secondary waves-effect waves-light'
              },
              buttonsStyling: false 
              });
            };
          }

        
    // Update Alert
    if (updatedAlertText) {
      updatedAlertText.onclick = function () {
        Swal.fire({
          title: 'Are you Sure?',
          text: 'Alert details will be updated',
          icon: 'success', 
        showCancelButton: true,
        confirmButtonText: 'Yes, Proceed',
        customClass: {
          confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
          cancelButton: 'btn btn-label-secondary waves-effect waves-light'
        },
        buttonsStyling: false 
        });
      };
    }
    
    // Update Alert
    if (iconUpdate) {
      iconUpdate.onclick = function () {
        Swal.fire({
          title: 'Are you Sure?',
          text: 'Camera details will be updated',
          icon: 'success', 
        showCancelButton: true,
        confirmButtonText: 'Yes, Proceed',
        customClass: {
          confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
          cancelButton: 'btn btn-label-secondary waves-effect waves-light'
        },
        buttonsStyling: false 
        });
      };
    }

    // Alert With Functional Confirm Button
    if (confirmDelete) {
      confirmDelete.onclick = function () {
        Swal.fire({
          title: 'Are you sure?',
          text: "Camera details will be deleted permanently",
          icon: 'error',
          showCancelButton: true,
          confirmButtonText: 'Yes, Proceed!',
          customClass: {
            confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
            cancelButton: 'btn btn-label-secondary waves-effect waves-light'
          },
          buttonsStyling: false
        }).then(function (result) {
          if (result.value) {
            Swal.fire({
              icon: 'success',
              title: 'Deleted!',
              text: 'Camera details deleted successfully.',
              customClass: {
                confirmButton: 'btn btn-success waves-effect waves-light'
              }
            });
          }
        });
      };
    }
 
     // Section Delete Confirm Button
     if (sectionDelete) {
      sectionDelete.onclick = function () {
        Swal.fire({
          title: 'Are you sure?',
          text: "Section details will be deleted permanently",
          icon: 'error',
          showCancelButton: true,
          confirmButtonText: 'Yes, Proceed!',
          customClass: {
            confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
            cancelButton: 'btn btn-label-secondary waves-effect waves-light'
          },
          buttonsStyling: false
        }).then(function (result) {
          if (result.value) {
            Swal.fire({
              icon: 'success',
              title: 'Deleted!',
              text: 'Section details deleted successfully.',
              customClass: {
                confirmButton: 'btn btn-success waves-effect waves-light'
              }
            });
          }
        });
      };
    }


      // Group Delete Confirm Button
      if (groupDelete) {
        groupDelete.onclick = function () {
          Swal.fire({
            title: 'Are you sure?',
            text: "Group details will be deleted permanently",
            icon: 'error',
            showCancelButton: true,
            confirmButtonText: 'Yes, Proceed!',
            customClass: {
              confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
              cancelButton: 'btn btn-label-secondary waves-effect waves-light'
            },
            buttonsStyling: false
          }).then(function (result) {
            if (result.value) {
              Swal.fire({
                icon: 'success',
                title: 'Deleted!',
                text: 'Group details deleted successfully.',
                customClass: {
                  confirmButton: 'btn btn-success waves-effect waves-light'
                }
              });
            }
          });
        };
      }

  // Info Alert
  if (iconInfo) {
    iconInfo.onclick = function () {
      Swal.fire({
        title: 'Info!',
        text: 'You clicked the button!',
        icon: 'info',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Warning Alert
  if (iconWarning) {
    iconWarning.onclick = function () {
      Swal.fire({
        title: 'Warning!',
        text: ' You clicked the button!',
        icon: 'warning',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Error Alert
  if (iconError) {
    iconError.onclick = function () {
      Swal.fire({
        title: 'Error!',
        text: ' You clicked the button!',
        icon: 'error',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Question Alert
  if (iconQuestion) {
    iconQuestion.onclick = function () {
      Swal.fire({
        title: 'Question!',
        text: ' You clicked the button!',
        icon: 'question',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Advanced Options
  // --------------------------------------------------------------------

  //Alert With Custom Icon
  if (customImage) {
    customImage.onclick = function () {
      Swal.fire({
        title: 'Sweet!',
        text: 'Modal with a custom image.',
        imageUrl: assetsPath + 'img/backgrounds/5.jpg',
        imageWidth: 400,
        imageAlt: 'Custom image',
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Auto Closing Alert
  if (autoClose) {
    autoClose.onclick = function () {
      var timerInterval;
      Swal.fire({
        title: 'Auto close alert!',
        html: 'I will close in <strong></strong> seconds.',
        timer: 2000,
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false,
        willOpen: function () {
          Swal.showLoading();
          timerInterval = setInterval(function () {
            Swal.getHtmlContainer().querySelector('strong').textContent = Swal.getTimerLeft();
          }, 100);
        },
        willClose: function () {
          clearInterval(timerInterval);
        }
      }).then(function (result) {
        if (
          // Read more about handling dismissals
          result.dismiss === Swal.DismissReason.timer
        ) {
          console.log('I was closed by the timer');
        }
      });
    };
  }

  // Close Alert On Backdrop Click
  if (outsideClick) {
    outsideClick.onclick = function () {
      Swal.fire({
        title: 'Click outside to close!',
        text: 'This is a cool message!',
        backdrop: true,
        allowOutsideClick: true,
        customClass: {
          confirmButton: 'btn btn-primary waves-effect waves-light'
        },
        buttonsStyling: false
      });
    };
  }

  // Alert With Steps
  if (progressSteps) {
    progressSteps.onclick = function () {
      const steps = ['1', '2', '3'];
      const swalQueueStep = Swal.mixin({
        confirmButtonText: 'Forward',
        cancelButtonText: 'Back',
        progressSteps: steps,
        input: 'text',
        inputAttributes: {
          required: true
        },
        validationMessage: 'This field is required'
      });

      async function backAndForward() {
        const values = [];
        let currentStep;

        for (currentStep = 0; currentStep < steps.length; ) {
          const result = await new swalQueueStep({
            title: 'Question ' + steps[currentStep],
            showCancelButton: currentStep > 0,
            currentProgressStep: currentStep
          });

          if (result.value) {
            values[currentStep] = result.value;
            currentStep++;
          } else if (result.dismiss === 'cancel') {
            currentStep--;
          }
        }

        Swal.fire(JSON.stringify(values));
      }

      backAndForward();
    };
  }


      

  // Alert With Ajax Request
  if (ajaxRequest) {
    ajaxRequest.onclick = function () {
      var deps = document.getElementById("usecase").value;

      Swal.fire({
        title: 'Do you want to get the report',
        // input: 'text',        
        text: deps,
        inputAttributes: {
          autocapitalize: 'off'
        },
        showCancelButton: true,
        confirmButtonText: 'Yes, Proceed',
        showLoaderOnConfirm: true,
        customClass: {
          confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
          cancelButton: 'btn btn-label-danger waves-effect waves-light'
        },
        preConfirm: login => {
          return fetch('//api.github.com/users/' + login)
            .then(response => {
              if (!response.ok) {
                throw new Error(response.statusText);
              }
              return response.json();
            })
            .catch(error => {
              Swal.showValidationMessage('Request failed:' + error);
            });
        },
        backdrop: true,
        allowOutsideClick: () => !Swal.isLoading()
      }).then(result => {

        if (deps == 'Select Use Case' || deps == '') {
          Swal.fire({
            icon: 'warning',
            title: 'Error!',
            text: 'Please select use case.',
            customClass: {
              confirmButton: 'btn btn-success waves-effect waves-light'
            }
          });
        }        
        else if (result.isConfirmed && deps == 'People Occupancy') {
          window.location.href = 'report-people-occupancy.php';   
          return deps;       
        }
        else if (result.isConfirmed && deps == 'Vehicle Occupancy') {
          window.location.href = 'report-vehicle-occupancy.php';          
          return deps;
        }        
        else if (result.isConfirmed && deps == 'Intrusion') {
          window.location.href = 'report-intrusion.php';          
          return deps;
        }        
        else if (result.isConfirmed && deps == 'Loitering') {
          window.location.href = 'report-loitering.php';          
          return deps;
        }        
        else if (result.isConfirmed && deps == 'Queue Management') {
          window.location.href = 'report-queue.php';          
          return deps;
        }        
        else if (result.isConfirmed && deps == 'Dwell Time') {
          window.location.href = 'report-dwell.php';          
          return deps;
        }        
        else if (result.isConfirmed && deps == 'Heat Map') {
          window.location.href = 'report-heat.php';          
          return deps;
        }                                                
        else {
          Swal.fire({
            icon: 'warning',
            title: 'Not Found!',
            text: 'Use Case report not found.',
            customClass: {
              confirmButton: 'btn btn-success waves-effect waves-light'
            }
          });      
      }
      });
    };
  }

  // Alert With Functional Confirm Button
  if (confirmText) {
    confirmText.onclick = function () {
      Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, delete it!',
        customClass: {
          confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
          cancelButton: 'btn btn-label-secondary waves-effect waves-light'
        },
        buttonsStyling: false
      }).then(function (result) {
        if (result.value) {
          Swal.fire({
            icon: 'success',
            title: 'Deleted!',
            text: 'Your file has been deleted.',
            customClass: {
              confirmButton: 'btn btn-success waves-effect waves-light'
            }
          });
        }
      });
    };
  }


    // Alert With Functional Submit Button
    if (submitText) {
      submitText.onclick = function () {
        Swal.fire({
          title: 'Are you sure?',
          text: "Use Case details will be saved",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Yes, Submit',
          customClass: {
            confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
            cancelButton: 'btn btn-label-secondary waves-effect waves-light'
          },
          buttonsStyling: false
        }).then(function (result) {
          if (result.value) {
            Swal.fire({
              icon: 'success',
              title: 'Saved!',
              text: 'Use Case details saved successfully',
              customClass: {
                confirmButton: 'btn btn-success waves-effect waves-light'
              }
            }).then(function() {
              // Redirect to another page
              window.location.href = 'cases.php';
            });
          }
        });
      };
    }


    // Alert With Functional updated Button
    if (updatedText) {
      updatedText.onclick = function () {
        Swal.fire({
          title: 'Are you sure?',
          text: "Use Case details will be updated",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Yes, Submit',
          customClass: {
            confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
            cancelButton: 'btn btn-label-secondary waves-effect waves-light'
          },
          buttonsStyling: false
        }).then(function (result) {
          if (result.value) {
            Swal.fire({
              icon: 'success',
              title: 'Saved!',
              text: 'Use Case details updated successfully',
              customClass: {
                confirmButton: 'btn btn-success waves-effect waves-light'
              }
            }).then(function() {
              // Redirect to another page
              window.location.href = 'cases.php';
            });
          }
        });
      };
    }


    
    // Alert With Functional Submit Button
    if (deleteText) {
      deleteText.onclick = function () {
        Swal.fire({
          title: 'Are you sure?',
          text: "Use Case details will be deleted permanently.",
          icon: 'error',
          showCancelButton: true,
          confirmButtonText: 'Yes, Submit',
          customClass: {
            confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
            cancelButton: 'btn btn-label-secondary waves-effect waves-light'
          },
          buttonsStyling: false
        }).then(function (result) {
          if (result.value) {
            Swal.fire({
              icon: 'success',
              title: 'Saved!',
              text: 'Use Case details deleted successfully',
              customClass: {
                confirmButton: 'btn btn-success waves-effect waves-light'
              }
            }).then(function() {
              // Redirect to another page
              window.location.href = 'cases.php';
            });
          }
        });
      };
    }

  // Alert With Functional Confirm Cancel Button
  if (confirmColor) {
    confirmColor.onclick = function () {
      Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, delete it!',
        customClass: {
          confirmButton: 'btn btn-primary me-3 waves-effect waves-light',
          cancelButton: 'btn btn-label-secondary waves-effect waves-light'
        },
        buttonsStyling: false
      }).then(function (result) {
        if (result.value) {
          Swal.fire({
            icon: 'success',
            title: 'Deleted!',
            text: 'Your file has been deleted.',
            customClass: {
              confirmButton: 'btn btn-success waves-effect waves-light'
            }
          });
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          Swal.fire({
            title: 'Cancelled',
            text: 'Your imaginary file is safe :)',
            icon: 'error',
            customClass: {
              confirmButton: 'btn btn-success waves-effect waves-light'
            }
          });
        }
      });
    };
  }
})();
