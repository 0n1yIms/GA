#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <thread>

const double g = 9.81;        // Gravedad (m/s^2)
const double dt = 0.01;       // Intervalo de tiempo (s)
const double stiffness = 0.1; // Rigidez de la cuerda
const int numParticles = 10;  // Número de partículas en la cuerda
const double segmentLength = 1.0; // Longitud entre partículas

struct Particle {
    double x, y;    // Posición de la partícula
    double vx, vy;  // Velocidad de la partícula
    bool fixed;     // Si la partícula está fija (en un punto de anclaje)

    Particle(double posX, double posY, bool isFixed = false)
        : x(posX), y(posY), vx(0), vy(0), fixed(isFixed) {}
};

void aplicarGravedad(Particle &p) {
    if (!p.fixed) {
        p.vy += g * dt;
    }
}

void actualizarParticula(Particle &p) {
    if (!p.fixed) {
        p.x += p.vx * dt;
        p.y += p.vy * dt;
    }
}

void aplicarRestriccion(Particle &p1, Particle &p2) {
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    double dist = std::sqrt(dx * dx + dy * dy);
    double diff = (dist - segmentLength) / dist;

    if (!p1.fixed) {
        p1.x += stiffness * diff * dx;
        p1.y += stiffness * diff * dy;
    }
    if (!p2.fixed) {
        p2.x -= stiffness * diff * dx;
        p2.y -= stiffness * diff * dy;
    }
}

void dibujarCuerda(const std::vector<Particle> &particles) {
    system("clear"); // Limpia la pantalla (en Windows usa system("cls"))
    for (int j = 0; j < 20; j++) {
        for (int i = 0; i < 40; i++) {
            bool particleFound = false;
            for (const auto &p : particles) {
                if (static_cast<int>(p.x) == i && static_cast<int>(p.y) == j) {
                    std::cout << "O";
                    particleFound = true;
                    break;
                }
            }
            if (!particleFound) std::cout << ".";
        }
        std::cout << std::endl;
    }
}

int main() {
    std::vector<Particle> particles;

    // Inicializamos la cuerda en posición horizontal
    for (int i = 0; i < numParticles; i++) {
        particles.emplace_back(i * segmentLength, 0, i == 0); // La primera partícula está fija
    }

    while (true) {
        // Aplicamos la gravedad y actualizamos las partículas
        for (auto &p : particles) {
            aplicarGravedad(p);
            actualizarParticula(p);
        }

        // Aplicamos restricciones de distancia entre partículas adyacentes
        for (size_t i = 0; i < particles.size() - 1; i++) {
            aplicarRestriccion(particles[i], particles[i + 1]);
        }

        // Dibujamos la cuerda
        dibujarCuerda(particles);

        std::this_thread::sleep_for(std::chrono::milliseconds(50)); // Pausa
    }

    return 0;
}
